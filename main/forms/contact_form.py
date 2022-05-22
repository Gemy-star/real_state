from django import forms
from ..models import (
    Contact
)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('sent_at',)
        labels = {
            'name': 'الأسم',
            'message': 'الرسالة'
        }
