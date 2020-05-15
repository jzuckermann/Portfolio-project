from django.shortcuts import render

from contact.models import Contact

def contact(request):
    contact = Contact.objects
    return render(request, 'Portfolio/templates/ui-contact-us.html', {'contact':contact})
