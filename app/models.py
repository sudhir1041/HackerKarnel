from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    mobile=models.IntegerField()

    def __str__(self):
        return self.name
choice=[
    ('PENDING', 'Pending'),
    ('DONE', 'Done')
]

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task_detail=models.TextField()
    task_type=models.CharField(max_length=10,choices=choice,default='PENDING')

    def __str__(self):
        return self.task_detail
