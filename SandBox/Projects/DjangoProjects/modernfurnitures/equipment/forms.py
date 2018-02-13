from django import forms
from models import PostMessage, ASKER_CHOICES


class ContactusForm(forms.ModelForm):
    error_css_class = 'error'

    asker = forms.ChoiceField(choices=ASKER_CHOICES, required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'What\'s your name?'}), required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'john@example.com'}), required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Phone number to call You!!'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Topic of Question'}), required=True)
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Message to us'}), required=True)

    class Meta:
        model = PostMessage
        fields = "__all__"

