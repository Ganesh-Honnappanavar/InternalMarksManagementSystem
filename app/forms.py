from django import forms
from . models import iaMarks

class TopicForm(forms.ModelForm):
    class Meta:
        model = iaMarks
        fields = ['usnIA','sub_code','SEM','t1','t2','t3']
