from django import forms
from captcha.fields import ReCaptchaField

# provide support for HTML 5 input types

from django.forms.widgets import Input

class EmailInput(Input):
    input_type = 'email'

class TelInput(Input):
    input_type = 'tel'


# patch to provide HTML 5 "required" attributes to required inputs

#from django.forms.widgets import Widget, HiddenInput, FileInput
#from django.contrib.admin.widgets import AdminFileWidget

#old_build_attrs = Widget.build_attrs

#def build_attrs(self, extra_attrs=None, **kwargs):
    #attrs = old_build_attrs(self, extra_attrs, **kwargs)

    #if self.is_required and type(self) not in (AdminFileWidget, HiddenInput, FileInput) and "__prefix__" not in attrs["name"]:
        #attrs["required"] = "required"

    #return attrs

#Widget.build_attrs = build_attrs


# create forms

class ContactForm(forms.Form):

    SUBJECTS = (
        ('New Booking', 'Booking'),
        ('Service Enquiry', 'Enquiry'),
        ('Site Comment', 'Comment'),
    )

    subject = forms.ChoiceField(SUBJECTS)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(widget=EmailInput())
    phone = forms.CharField(widget=TelInput(), required=False)
    message = forms.CharField(widget=forms.Textarea, min_length=40, error_messages={'min_length':'Ensure that your message has at least 40 characters.'})
    cc_self = forms.BooleanField(required=False)
    captcha = ReCaptchaField(attrs={'theme': 'white'}, error_messages={'required':'Please enter the captcha code.', 'captcha_invalid':'Your Captcha code is invalid - please try again.'})
