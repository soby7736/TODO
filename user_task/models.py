from django.db import models

from user_app.models import *

# Create your models here.

class Task(models.Model):
    
    priority_choice = [('low','low'),
                      ('high','high'),]
    
    task_name = models.CharField(max_length=50)
    
    priority = models.CharField(max_length=50,choices=priority_choice)
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    is_complete = models.BooleanField(default=False)
    
    date_created = models.DateTimeField(auto_now_add=True)