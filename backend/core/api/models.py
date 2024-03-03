from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
import pytz
# one to many relationship madel that is many will have forign key here post will have user as foreign key

class Post(models.Model) :
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 1000)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post_at = models.DateTimeField(db_default = datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
    status = models.CharField(max_length=20, choices=[('scheduled', 'Scheduled'), ('published', 'Published')], default='published')

    def is_to_be_posted(self) :
        return datetime.datetime.now(pytz.timezone('Asia/Kolkata')) >= self.post_at

    def __str__(self)  :
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"
