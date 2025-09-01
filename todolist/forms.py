 # whenever we are taking an input that is related to our database, we can just write short codes and connect with our database
from django import forms
from .models import Todolist

class Todoform(forms.ModelForm):
   class Meta:
       model=Todolist
       fields=["task","done"]
    