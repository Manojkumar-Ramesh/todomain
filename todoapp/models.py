from django.db import models

# Create your models here.

class Acitivity(models.Model):
    title=models.CharField(max_length=200),
    created_date=models.DateTimeField(auto_now_add=True,blank=True)
    user=models.CharField(max_length=200)
    options=(
        ("In progress","In progress"),
        ("Completed","Completed"),
        ("Pending","Pending")
    )
    status=models.CharField(max_length=200,choices=options,default="Pending")


    def __str__(self):
        return self.title
