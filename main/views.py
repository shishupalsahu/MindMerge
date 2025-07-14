from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from main.forms import IdeaPostForm,CustomUserEditForm,ReviewForm
from main.models import IdeaPost,Review

from django.contrib.auth.models import User

from django.contrib import messages



# Create your views here.

def home(request):
    context = {
        'title':'homepage',
        'posts':IdeaPost.objects.all(),
        'postuser':User.objects.all(),
    }



    return render(request,'home.html',context)


def search(request):
    context = {
        'title':'searchpage',
    }

    searchuser = request.GET.get('username')

    if searchuser:
        results = User.objects.filter(username__icontains = searchuser)
        context["results"] = results

        if(len(results)<1):
            context['result']="No Data Found"

    else:
        context['result'] = "Search with User Name"

    return render(request, 'search.html', context)




@login_required(login_url='userlogin')
def profile(request):

    id = request.user
    context = {
        'title' : 'Profile Page',
        'user': request.user,
        'posts':IdeaPost.objects.filter(user_id=id)
    }

    return render(request,'profile.html',context)




@login_required(login_url='userlogin')
def addpost(request):
    context = {
        'title' : 'Add Post',
    }

    if request.method == "POST":
        addpost_form = IdeaPostForm(request.POST,request.FILES)

        if addpost_form.is_valid():
            addpost_form.save()
            return redirect('home')


        else:
            print(addpost_form.errors)
            context['form'] = IdeaPostForm(initial={'user_id':request.user})
            messages.error(request,"Erro While Uploading",addpost_form.errors)

    else:
        context['form'] = IdeaPostForm(initial={'user_id':request.user})


    return render(request,'addpost.html',context)



def userprofile(request,uid):

    context = {
        'title':'User Profile',
        'userdetails' : User.objects.get(id = uid),
        'userposts' : IdeaPost.objects.filter(user_id = uid),
    }

    return render(request,'userprofile.html',context)


def edituser(request, user_id):
    try:
        userdetails = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('home')

    if request.method == "POST":
        userform = CustomUserEditForm(request.POST, instance=userdetails)
        if userform.is_valid():
            userform.save()
            messages.success(request, "User details updated successfully.")
            return redirect('profile')
        else:
            messages.error(request, "Error updating user details.")
    else:
        userform = CustomUserEditForm(instance=userdetails)

    context = {
        'title': 'user Update',
        'form': userform
    }
    return render(request, 'edituser.html', context)



def editpost(request,post_id):

    try:
        postdetails = IdeaPost.objects.get(id=post_id)
    except IdeaPost.DoesNotExist:
        return redirect('home')
    
    if request.method == "POST":
        postform = IdeaPostForm(request.POST, request.FILES, instance=postdetails)
        if postform.is_valid():
            postform.save()
            return redirect('profile')
    else:
        postform = IdeaPostForm(instance=postdetails)

    context = {
        'title':'Edit Post',
        'form': postform,
    }

    return render(request,'editpost.html',context)  



def deletepost(request,post_id):
    postdetails = IdeaPost.objects.get(id=post_id)
    postdetails.delete()
    return redirect('profile')




@login_required(login_url='userlogin')
def review(request,post_id):

    context={
        'title':'reviewpage',
        'form' : ReviewForm(initial={'reviewer_id':request.user.id,'post_id':post_id}),
    }

    postdetails = IdeaPost.objects.get(id=post_id)
    context['post'] = postdetails

    reviews = Review.objects.filter(post_id=post_id)
    context['reviews'] = reviews

    if request.method == "POST":
        review = ReviewForm(request.POST)
        if review.is_valid():
            review.save()

    return render(request,'reviewpage.html',context)


def deletereview(request,review_id):
    review = Review.objects.get(id=review_id)
    post_id = review.post_id.id
    review.delete()

    return redirect('review', post_id=post_id)
