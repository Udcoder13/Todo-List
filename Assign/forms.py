from django.forms import ModelForm
from.models import task

class CreateTask(ModelForm):
      class Meta:
        model = task
        fields=['task_name', 'task_description', 'task_date']

class UpdateForm(ModelForm):
    
    class Meta:
        model = task
        fields = ['task_name', 'task_date']
