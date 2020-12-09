from django.db import models
from topic.models import Topic
from users.models import User


# Create your models here.
class Message(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(User,
                                     on_delete=models.CASCADE)
    parent_message = models.IntegerField(default=0)
    content = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
