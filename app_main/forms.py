from django.forms import ModelForm, CharField
from ckeditor.fields import CKEditorWidget

from .models import Homework


class HomeworkForm(ModelForm):
    body = CharField(widget=CKEditorWidget())

    class Meta:
        model = Homework
        fields = ['title', 'body', 'file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({ 'class': 'border border-slate-100 rounded px-2 py-1 outline', 'placeholder': 'Title' })
        self.fields['body'].widget.attrs.update({ 'class': 'border border-slate-100 rounded px-2 py-1 outline', 'placeholder': 'Homework description' })
        self.fields['file'].widget.attrs.update({ 'class': 'border border-slate-100 rounded px-2 py-1 outline', 'placeholder': 'File' })
