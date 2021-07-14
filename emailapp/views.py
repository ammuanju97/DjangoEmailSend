from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

from .forms import EmailForm

# Create your views here.
def index(request):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = 'resume'
            message = 'sending resuem'
            recipient = form.cleaned_data.get('email')
            send_mail(subject,
                message, settings.EMAIL_HOST_USER , [recipient],
                fail_silently=False)
            messages.success(request, 'sucess!')
            return redirect('index')
    return render(request, 'emailapp/index.html', {'form' : form})