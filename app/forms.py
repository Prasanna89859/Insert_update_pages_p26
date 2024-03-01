from django  import forms
from app.models import *

class Topic_nameForm(forms.Form):
    topic_name=forms.CharField()

class Webpagesforms(forms.Form):
    tl=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
    Topic=forms.ChoiceField(choices=tl)
    name=forms.ChoiceField()
    url=forms.URLField()

class AccessRecordForm(forms.Form):
    w1=[[to.topic_name,to.topic_name] for to in Webpage.objects.all()]
    name=forms.ChoiceField(choices=w1)  
    date=forms.DateField()
    author=forms.CharField()
    

    
