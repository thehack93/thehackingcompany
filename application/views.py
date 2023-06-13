from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import *
# Create your views here.
def index(request):
    services = Service.objects.all()
    context = {
        "services" : services
    }
    return render(request,"application/index.html",context)

def services(request):
    services = Service.objects.all()
    context = {
        "services" : services
    }
    return render(request,"application/services.html",context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Create a new Contact instance
        contact = Contact(name=name, email=email, phone=phone, message=message)

        # Save the contact to the database
        contact.save()
        
        # Perform validation and additional processing if needed
        
        
        # Specify the list of additional email recipients
        additional_recipients = ['embusinessintelligence@gmail.com']

        # Build the email body
        email_body = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'

        # Combine the additional recipients list with the default email sender
        recipients = [settings.DEFAULT_FROM_EMAIL] + additional_recipients

        # Send the email to all recipients
        send_mail(
            'Contact Form Submission',
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            recipients,
            fail_silently=False,
        )
        return redirect("/contact")
    return render(request,"application/contact.html")
def pricing(request):
    return render(request,"application/pricing.html")
def about(request):
    return render(request,"application/about.html")