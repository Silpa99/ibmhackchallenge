from django import forms
from .models import *
from django.contrib.auth import (
    authenticate,
    get_user_model

)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = [
            'username',
            'email',
            'password',
            'phoneno',
            'dob',
            'upload_your_resume'
            
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        #password2 = self.cleaned_data.get('password2')
        #if password1 != password2:
        #    raise forms.ValidationError("Password must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)






class AddSkillsForm(forms.ModelForm):
    Skill = forms.CharField(label='Skill name')

    class Meta:
        model = Skills
        fields = [
            'skill_name',
            'jobs'
            
        ]

class RecruiterForm(forms.ModelForm):
    class Meta:
        model=Job_postings
        fields=['title']

class AddSkillsForm(forms.ModelForm):
    #skill = forms.CharField(label='Skill name')
    #jobs = forms.ManyToManyField(Job_postings)

    class Meta:
        model = Skills
        fields = [
            'skill_name',
            'jobs'
            
        ]

class JobPostForm(forms.ModelForm):

    class Meta:
        model = Job_postings
        fields = ['company', 
    'title' ,
    'description' ,
    'job_address' ,
        ]


