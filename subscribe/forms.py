from django import forms
from django.utils.translation import gettext_lazy as _
from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields = '__all__'
        # exclude=('firstname',)
        labels= {
            'firstname': _('Enter First Name'),
            'lastname': _('Enter Last Name'),
            'email': _('Enter Email address')
        }
        # help_texts = {
        #     'firstname': _('Enter characters only.'),
        #     'lastname': _('Enter your last name.'),
        #     'email': _('Enter a valid email address.')
        # }
        error_messages = {
            'email': {
                'required': _('Email is required.'),
                'invalid': _('Enter a valid email address.')
            },
            'firstname': {
                'max_length': _('First name cannot exceed 100 characters.'),
                'required': _('First name is required,Cannot move forward.')
            },
            'lastname': {
                'max_length': _('Last name cannot exceed 100 characters.')
            }
        }

# def validate_characters(value):
#     if not value.isalpha():
#         raise forms.ValidationError("This field should contain only characters.")
    
# class SubscribeForm(forms.ModelForm):
    # firstname = forms.CharField(max_length=100, required=False, label='First Name',help_text='Enter Character only')
    # lastname = forms.CharField(max_length=100, required=False, label='Last Name',help_text='Enter Character only',validators=[validate_characters])
    # email = forms.EmailField(max_length=254, required=True, label='Email Address',help_text='Enter a valid email address') 
    
    
    
    # def clean_firstname(self):
    #     data = self.cleaned_data['firstname']
    #     if not data.isalpha():
    #         raise forms.ValidationError("First name should contain only characters.")
    
