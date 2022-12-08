from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    user_image = models.ImageField(null=True, blank=True, upload_to="images/")

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return f"First name: {self.first_name} Last name: {self.last_name} E-mail: {self.email}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    post_id = models.AutoField(primary_key=True)
    post_content = models.TextField(max_length=300)
    post_date = models.DateTimeField(editable=False)
    post_reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='PostHasReplies')  
    # post_likes = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='PostHasLikes')  

    def _replies(self):
        return type(self).objects.filter(post_id__in=self.post_reply.all())  # type: ignore

    # def _likes(self):
    #     return type(self).objects.filter(post_id__in=self.post_likes.all())  # type: ignore

    def __str__(self):
        return f"User: {User.username} Content: {self.post_content}"

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    like_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f"User: {User.username}"
