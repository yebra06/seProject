from django import forms
from django.conf import settings

from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Field, Layout, Submit

from .models import User


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('email', placeholder='Email', required=True),
            Field('password', placeholder='Password', required=True),
            Submit('submit', 'Submit'))


class SignupForm(LoginForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        email_query = User.objects.filter(email=email)
        if email_query.exists():
            raise forms.ValidationError('This email has already been registered')
        return email
