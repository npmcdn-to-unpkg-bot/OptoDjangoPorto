from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

from .forms import ContactForm


def index(request):
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
            contact_subject = form.cleaned_data['subject']
            contact_message = form.cleaned_data['message']
            #contact_message += "\nContact: \nFirst name: " + contact_fname
            #contact_message += "\nLast name:\n " + contact_lname
            #contact_message += "\nMessage :\n" + contact_message

            # email to customer
            plaintext = get_template('templates/apps/static_pages/contact_us/email.txt')
            htmly = get_template('templates/apps/static_pages/contact_us/email.html')

            ctx = {'fname': contact_fname, 'lname': contact_lname, 'subject': contact_subject,
                           'message': contact_message}

            text_content = plaintext.render(ctx)
            html_content = htmly.render(ctx)

            from_email = settings.EMAIL_OPTOLOGIC_SENDER
            to_email = [contact_email, settings.EMAIL_OPTOLOGIC_RECEIVER]

            email = EmailMultiAlternatives(contact_subject, text_content, from_email, to_email)
            email.attach_alternative(html_content, "text/html")
            email.send()
            message_posted = True

            # TODO bloc message remerciements à faire, acheter image :D
            return render(request, 'templates/apps/static_pages/contact_us/contact_us.html',
                          {'form': form, 'message_posted': message_posted, 'firstname': contact_fname})


    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    message_posted = False
    return render(request, 'templates/apps/static_pages/contact_us/contact_us.html',
                  {'form': form, 'message_posted': message_posted, 'firstname': None})
