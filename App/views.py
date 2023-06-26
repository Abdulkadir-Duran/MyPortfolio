from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def index(request):
    home = Home.objects.all()
    texts = About.objects.all()
    projectsML = ProjectsML.objects.all()
    projectswebs = ProjectsWeb.objects.all()
    projects = Projects.objects.all()
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]

            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["email"]
            message = form.cleaned_data['message']

            try:
                send_mail(subject=subject,message=message, from_email=from_email, recipient_list=["abdulkadir5035190144@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, 'index.html', {'homeInfo':home, 'aboutInfo': texts, 'ProjectsML': projectsML,
    'projectswebs': projectswebs, 'projectboxes': projects, 'form': form

    })
def messageSent(request):
    form = ContactForm()
    
    return render(request, 'result.html', {'succcess': 'Email Successfully sent! Thank you for your message.'})