from django import forms
from .models import Problem,Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = [
            "title",
            "body",
            "tag",
        ]

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Adding an attribute to the <input> tag for a django ModelForm field'}),
        }

        labels = {
            "title": "Title Of The Problem (Be Specific):",
            "body": "Body (Full Details About The Problem):",
        }

    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all().order_by('name'),widget=forms.CheckboxSelectMultiple)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == "tag":
                continue
            else:
                self.fields[field].widget.attrs.update({
                'class': 'form-control mb-1'
    })
