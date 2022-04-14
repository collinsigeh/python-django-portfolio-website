from email import message
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail

# Create your views here.
def home(request):
    """Displays the home page"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        name = name.strip().title()
        email = email.strip().lower()
        message = message.strip()
        send_mail(
            'New message',
            f'Hello admin,\n\n{name} sent you a message with the following details:\n\nMessage:\n{message}\n\nContact email: {email}',
            'ci@inspireyougroup.com',
            ['ci@inspireyougroup.com'],
            fail_silently=False,
        )
    return render(request, 'index.html')