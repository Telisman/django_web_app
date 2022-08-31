from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from clients.models import ClientsUsers, UserWorkExperience, UserEducation
from django import forms
from django.forms import ModelForm


class SingUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ClientsUsers
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


class AddWork(ModelForm):
    class Meta:
        model = UserWorkExperience
        fields = ('user',
                  'experience1',
                  'experience2',
                  'experience3',
                  'experience4',
                  'start_date_experience1',
                  'start_date_experience2',
                  'start_date_experience3',
                  'start_date_experience4',
                  'end_date_experience1',
                  'end_date_experience2',
                  'end_date_experience3',
                  'end_date_experience4',
                  )

        widgets = {
            'experience1': forms.TextInput(attrs={'class': 'form-control'}),
            'experience2': forms.TextInput(attrs={'class': 'form-control'}),
            'experience3': forms.TextInput(attrs={'class': 'form-control'}),
            'experience4': forms.TextInput(attrs={'class': 'form-control'}),

            'start_date_experience1': forms.DateInput(attrs={'class': 'form-control'}),
            'start_date_experience2': forms.DateInput(attrs={'class': 'form-control'}),
            'start_date_experience3': forms.DateInput(attrs={'class': 'form-control'}),
            'start_date_experience4': forms.DateInput(attrs={'class': 'form-control'}),

            'end_date_experience1': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date_experience2': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date_experience3': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date_experience4': forms.DateInput(attrs={'class': 'form-control'}),

            'user': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),

        }


class EducationForm(ModelForm):
    class Meta:
        model = UserEducation
        fields = (
            'user',
            'education_high_school',
            'start_date_high_school',
            'end_date_high_school',
            'education_university',
            'start_date_university',
            'end_date_university',
        )
        widgets = {
            'education_high_school': forms.TextInput(attrs={'class': 'form-control'}),
            'education_university': forms.TextInput(attrs={'class': 'form-control'}),

            'start_date_high_school': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date_high_school': forms.DateInput(attrs={'class': 'form-control'}),
            'start_date_university': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date_university': forms.DateInput(attrs={'class': 'form-control'}),

            'user': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
        }
