from django.db import models

# Create your models here.
class Todolist(models.Model):
    task=models.CharField(max_length=500)
    done=models.BooleanField(default=False)
    #now this model is cuurently in our file only so we need to perform migrations
    
    def __str__(self): 
        return self.task + " "+str(self.done)
 