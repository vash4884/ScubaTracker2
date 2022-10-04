from django import forms
#from django.forms.util import ErrorList
from django.core.exceptions import ValidationError
from tracker.models import instructor
import re

class instructorNameForm(forms.ModelForm):
   name = forms.CharField(max_length=250, required=True, label="Enter Instructors name")

   class Meta:
        model = instructor
        exclude = ['instructorID',]
