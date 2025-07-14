from django import forms

from main.models import IdeaPost
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from main.models import Review

class IdeaPostForm(forms.ModelForm):
    class Meta:
        model = IdeaPost
        fields = '__all__'

        widgets = {

            'user_id': forms.TextInput(attrs={'type':'hidden'}),

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            
            'description': forms.Textarea(attrs={'class': 'form-control', 'maxlength': '500','placeholder': 'Max 450 words'}),
            
            'image': forms.ClearableFileInput(attrs={'class': 'form-control','accept':'image/*,video/*'}), 

            'document': forms.ClearableFileInput(attrs={'class': 'form-control','accept':'.pdf,.doc,.docx'}),
            
        }


class CustomUserEditForm(UserChangeForm):
        class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email')


class ReviewForm(forms.ModelForm):
     class Meta:
          model = Review
          fields = '__all__'
          widgets = {
               'post_id':forms.TextInput(attrs={'type':'hidden'}),
               'reviewer_id':forms.NumberInput(attrs={'type':'hidden'}),
               'review' : forms.Textarea(attrs={'placeholder':'Write your Review here'})
          }