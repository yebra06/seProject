from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit

from .models import Profile


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
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
        email_query = Profile.objects.filter(email=email)
        if email_query.exists():
            raise forms.ValidationError('This email has already been registered')
        return email


class UserForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'user-info-form'
        self.helper.form_class = 'user-info-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'user-info'
        self.helper.layout = Layout(
            Field('first_name', placeholder=self.instance.first_name or 'first name'),
            Field('last_name', placeholder=self.instance.last_name or 'last name'),
            Field('email', placeholder=self.instance.email, required=False),
            Submit('submit', 'Submit'))
