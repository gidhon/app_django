from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from base.forms import ContactForm


# handles the contact form
def contact(request):

    if request.method == 'POST':

        f = ContactForm(request.POST)

        if f.is_valid():
            subject    = f.cleaned_data['subject']
            first_name = f.cleaned_data['first_name']
            last_name  = f.cleaned_data['last_name']
            sender     = f.cleaned_data['email']
            phone      = f.cleaned_data['phone']
            message    = f.cleaned_data['message']
            cc_self    = f.cleaned_data['cc_self']

            recipients = ['bookings@example.com']

            if cc_self:
                recipients.append(sender)

            c = {
                'subject': subject,
                'first_name': first_name,
                'last_name': last_name,
                'sender': sender,
                'phone': phone,
                'message': message
                }

            # parse strings and create template objects, pair with context

            text_version = render_to_string('base/contact/email.txt', c)
            html_version = render_to_string('base/contact/email.html', c)

            # subclass EmailMessage with EmailMultiAlternatives and send

            mail = EmailMultiAlternatives(subject, text_version, '', recipients)
            mail.attach_alternative(html_version, 'text/html')
            mail.send()

            return HttpResponseRedirect('/contact/thanks/')

        else:
            f  = ContactForm(request.POST)
            t  = 'base/contact/contact.html'
            c1 = {'form': f}
            c2 = RequestContext(request)

            return render_to_response(t, c1, c2)

    else:

        f  = ContactForm()
        t  = 'base/contact/contact.html'
        c1 = {'form': f}
        c2 = RequestContext(request)

    return render_to_response(t, c1, c2)
