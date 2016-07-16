__author__ = 'egoo'

from django.forms import ModelForm
from .models import Comments

class CommentForm(ModelForm):
    class Meta:                              # class Meta - позволяет описать некоторые риквизиты модели
        model = Comments
        exclude = []
        fields = ['text']