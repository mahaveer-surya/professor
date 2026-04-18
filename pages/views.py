# pages/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()

            # Send Email
            send_mail(
                subject=f"New Contact: {contact.subject}",
                message=contact.message,
                from_email=contact.email,
                recipient_list=['your_email@gmail.com'],
            )

            messages.success(request, "Message sent successfully!")
            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})