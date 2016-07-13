from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import get_template

from .forms import ContactForm


def index(request):
    template = get_template('templates/apps/contact_us/email.html')
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            contact_fname = form.cleaned_data['first_name']
            contact_lname = form.cleaned_data['last_name']
            contact_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            contact_message = form.cleaned_data['message']
            message = "Essai message contact\n\nFirst name: " + contact_fname
            message += "\nLast name: " + contact_lname
            message += "\nMessage :\n" + contact_message

            # TODO template pour le mail
            recipients = settings.EMAIL_OPTOLOGIC_SENDER
            contact_email = [contact_email, settings.EMAIL_OPTOLOGIC_RECEIVER ]
            email = EmailMessage(subject, message, recipients, contact_email)
            email.send()
            print(form)
            message_posted = True
            # TODO bloc message remerciements à faire
            return render(request, 'templates/apps/static_pages/contact_us/contact_us.html',  {'form': form, 'message_posted' : message_posted, 'firstname' : contact_fname})


    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    message_posted = False
    return render(request, 'templates/apps/static_pages/contact_us/contact_us.html',  {'form': form, 'message_posted' : message_posted, 'firstname' : None})