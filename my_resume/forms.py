from django import forms

from .models import Message

class MessageForm(forms.ModelForm):
    '''
    Creating a form to collect message from visitors
    Alternative for forms.Form
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4,
    }))
    '''
    class Meta:
        model = Message
        fields = ['name', 'email', 'message',]
