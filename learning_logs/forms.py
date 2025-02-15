from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta: # типу визначення характеристик Форми (або моделі)
        model = Topic
        fields = ['text']
        labels = {'text': ''}