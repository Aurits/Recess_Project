from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


from .models import InstructorFeedback, Course


class InstructorForm(forms.ModelForm):
    class Meta:
        model = InstructorFeedback
        fields = ['instructorName', 'department', 'courseUnit', 'knowledge', 'communication', 'teachingStyle',
                  'responsiveness', 'additional_comments']

        widgets = {
            'instructorName': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'courseUnit': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'knowledge': forms.RadioSelect(attrs={'class': 'd-flex', 'required': True}),
            'communication': forms.RadioSelect(attrs={'class': 'd-flex', 'required': True}),
            'teachingStyle': forms.RadioSelect(attrs={'class': 'd-flex', 'required': True}),
            'responsiveness': forms.RadioSelect(attrs={'class': 'd-flex', 'required': True}),
            'additional_comments': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
        }


from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['courseName', 'courseCode', 'courseDescription', 'effectiveness', 'interest', 'improvement']
        widgets = {
            'courseName': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'courseCode': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'courseDescription': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
            'effectiveness': forms.RadioSelect(attrs={'class': 'd-flex', 'required': True}),
            'interest': forms.RadioSelect(attrs={'class': 'd-flex', 'required': True}),
            'improvement': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
        }
