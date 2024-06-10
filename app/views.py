from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Customer, Applicant

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("About page.")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("Services page.")

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        company = request.POST['company']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        if Customer.objects.filter(email=email).exists():
            messages.info(request,"Customer already exists.")
            return redirect('contact')
        else:  
            customer = Customer.objects.create(name=name, company=company,email=email,phone=phone, desc=desc)
            return send_email(request,name,email,'contact')
           
    else:
        return render(request,'contact.html')


def careers(request):
    return render(request, 'careers.html')

def form_submitted(request):
    return render(request,'form_submitted.html')

def data_analyst(request):
    return render(request,'careers/data_analyst.html')

def it_consultant(request):
    return render(request,'careers/it_consultant.html')

def network_engineer(request):
    return render(request,'careers/network_engineer.html')

def project_manager(request):
    return render(request,'careers/project_manager.html')

def senior_software_engineer(request):
    return render(request,'careers/senior_software_engineer.html')

def application(request):
    return render(request,'careers/application.html')

def submit_application(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        position = request.POST['position']
        resume = request.FILES['resume']
        
        # Handle form submission logic here
        #save the data and send an email
        if Applicant.objects.filter(email=email).exists():
            messages.info(request, "Already exists.")
            return redirect('application')
        else:
            applicant = Applicant.objects.create(name=name, email=email, phone=phone, position = position, resume=resume)
            return send_email(request, name, email,'application')
    else:
        return render(request, 'careers/application.html')
    

def send_email(request,name,email, context):
    if context == 'contact':
        subject = f'Thank you for contacting us, {name}!'
        message = f'Dear {name},\n\nThank you for reaching out to us. We have received your inquiry and will get back to you shortly.\n\nBest regards,\nAzayd Consulting Team'
    elif context == 'application':
        subject = f'Thank you for applying, {name}!'
        message = f'Dear {name},\n\nThank you for applying for a position at Azayd Consulting. We have received your application and will review it shortly.\n\nBest regards,\nAzayd Consulting Team'
    recipient_list = [email]
    try:
        send_mail(subject, message, 'yourcompany@example.com', recipient_list)
        return HttpResponseRedirect(reverse('form_submitted')) 
    except Exception as e:
        messages.error(request, "An error occurred while sending the email. Please try again later.")
        return HttpResponseRedirect(reverse('contact') if context == 'contact' else reverse('application'))