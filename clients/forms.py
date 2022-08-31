from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from clients.models import ClientsUsers
from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime, AdminDateWidget


class SingUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ClientsUsers
        # widgets = {"date_of_birth":AdminDateWidget()}
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'user_type',
            'date_of_birth',
            'gender')

    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)
        self.fields['user_type'].required = True
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'


class UserSettings(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ClientsUsers
        fields = ('username', 'first_name', 'last_name', 'email', 'bio', 'phone_number', 'profile_image')

    def __init__(self, *args, **kwargs):
        super(UserSettings, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].required = False
        self.fields['profile_image'].required = False
        self.fields['bio'].required = False
