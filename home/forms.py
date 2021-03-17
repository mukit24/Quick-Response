from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'full_name',
            'profile_picture',
            'batch',
            'student_id',
            'address',
            'mobile',
            'facebook'
        ]

        labels = {
            "address": "Address(Optional):",
            "mobile": "Mobile No(Optional):",
            "facebook":"Facebook Link(Optional):",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
            'class': 'form-control mb-1'})


class UpdateProfileForm(forms.Form):
    full_name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "value": "{{profile.full_name}}"
        })
    )
    # profile_pic = forms.FileField()
    # certificate = forms.FileField()
    # discipline = forms.ChoiceField(choices=Discipline_Choices,widget=forms.Select(
    #     attrs={
    #        "class":"edit_profile_select",
    #     }
    # ))
    # student_id = forms.CharField(
    #     max_length=60,
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Enter Your Student ID"
    #     })
    # )
    # batch = forms.ChoiceField(choices=Batch_Choices,widget=forms.Select(
    #     attrs={
    #         "class":"edit_profile_select",
    #     }
    # ))
    # job_type = forms.CharField(
    #     max_length=60,
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Enter Your Job Type "
    #     })
       
    # )
    # job_posi = forms.CharField(
    #     max_length=60,
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Enter Your Position "
    #     })
    # )
    # company_name = forms.CharField(
    #     required=False,
    #     max_length=60,
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Enter Your Company Name"
    #     })
    # )
    
    # higher_study = forms.CharField(
    #     max_length=60,
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Enter Your Higher Study Information"
    #     })
    # )
    # present_address = forms.CharField(
    #     max_length=60,
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Enter Your Present Address"
    #     })
    # )
    # present_country = forms.ChoiceField(choices=Country_Choices,widget=forms.Select(
    #     attrs={
    #         "class":"edit_profile_select",
    #     }
    # ))
    # parmanent_address = forms.CharField(
    #     max_length=60,
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Enter Your Parmanent Address"
    #     })
    # )
    # mobile = forms.CharField(
    #     max_length=60,
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Enter Your Mobile Number"
    #     })
    # )
    # facebook = forms.URLField(
    #     max_length=60,
    #     required=False,
    #     widget=forms.URLInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Enter Your Facebook ID Link"
    #     })
    # )
    # linkdin = forms.URLField(
    #     max_length=60,
    #     required=False,
    #     widget=forms.URLInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Enter Your Linkdin Profile Link"
    #     })
    # )
    # # social_media_links = forms.URLField(
    # #     widget=forms.URLInput(attrs={
    # #         "class": "form-control",
    # #         "label": "Enter Your Social Media Links"
    # #     })
    # # )
    # about_me = forms.CharField(widget=forms.Textarea(
    #     attrs={
    #         "class": "form-control",
    #         "placeholder": "Write About You",
    #         "rows":2,
    #     })
    # )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
            'class': 'form-control mb-1'})

