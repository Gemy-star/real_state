from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView
from ..forms import ContactForm
from ..models import Contact


class ContactPageView(CreateView):
    template_name = 'main/contactpage/contact.html'
    form_class = ContactForm
    model = Contact

    def get_success_url(self):
        messages.success(self.request, "شكرا لتواصكم معنا سيتم الرد عليكم فى أقرب وقت ")
        return reverse('contact-page')