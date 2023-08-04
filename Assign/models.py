from django.db import models
from accounts.models import User
from django.contrib.auth import get_user_model


class task(models.Model):
      user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True)
      task_name=models.CharField(max_length=50)
      task_description=models.TextField()
      task_date=models.DateField(auto_now=False, auto_now_add=False)
      
      def __str__(self):
            return self.task_name
      
