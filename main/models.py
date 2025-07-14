from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class IdeaPost(models.Model):

    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField()

    image = models.FileField(upload_to='images/', blank=True, null=True)

    document = models.FileField(upload_to='documents/', blank=True, null=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    reviews = models.IntegerField(blank=True,null=True,default=0)




    def __str__(self):
        return self.title
    

class Review(models.Model):

    post_id = models.ForeignKey(IdeaPost,on_delete=models.CASCADE)
    reviewer_id = models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.TextField()
