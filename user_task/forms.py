from django import forms

from user_task.models import *

class TaskForm(forms.ModelForm):
    
    class Meta:
        
        model = Task
        
        fields = ["task_name","priority"]
