from django import forms
from .models import Problem

class PostForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = [
            "title",
            "body",
            "tag",
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
    })
