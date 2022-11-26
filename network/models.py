from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    user_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"First name: {self.first_name} Last name: {self.last_name} E-mail: {self.email}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    post_id = models.AutoField(primary_key=True)
    post_content = models.TextField(max_length=300)
    post_date = models.DateTimeField(editable=False)
    def __str__(self):
        return f"User: {User.username} Content: {self.post_content}"

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    post = models.ForeignKey(Post, on_delete=models.RESTRICT)
    def __str__(self):
        return f"User: {User.username} Content: {self.post.post_content}"
