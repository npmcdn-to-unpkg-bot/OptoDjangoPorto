from .forms import ContactForm
from OptoDjangoPorto import settings
from django.shortcuts import render
from django.core.mail import EmailMessage


# Create your views here.
def index(request):
    # define message posted as global variable
    # info - > http://stackoverflow.com/questions/16332326/unboundlocalerror-local-variable-a-referenced-before-assignment
    global message_posted

    template_name = 'apps/static_pages/contact_us/contact_us.html'

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
            message = "Essai message contact\n\nFirst name: " + contact_fname
            message += "\nLast name: " + contact_lname
            message += "\nMessage :" + form.cleaned_data['message']

            # TODO template pour le mail

            recipients = settings.EMAIL_OPTOLOGIC_SENDER
            contact_email = [contact_email, settings.EMAIL_OPTOLOGIC_RECEIVER ]

            email = EmailMessage(subject,message,recipients,contact_email)
            email.send()
            message_posted = True
            context = {
                'form': form,
                'message_posted': message_posted,
                'firstname': contact_fname
            }

            return render(request, template_name, context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
        message_posted = False

    context = {
        'form': form,
        'message_posted': message_posted,
        'firstname': None
    }
    return render(request, template_name, context)
