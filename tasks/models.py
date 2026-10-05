from django.db import models

# Create your models here.
class Task(models.Model):
    task_status=[
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]
    
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    status=models.CharField(max_length=20,choices=task_status,default="Pending")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def _str_(self):
        return f'{self.title}'