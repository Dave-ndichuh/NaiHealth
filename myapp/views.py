from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Appointment,Contact,Member
from myapp.forms import AppointmentForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
            username=request.POST['username'],
            password=request.POST['password'],
        ).exists():
            members = Member.objects.get(
                username=request.POST['username'],
                password=request.POST['password'],
            )
            return render(request, 'index.html', {'members': members})

        else:
            return render(request, 'login.html') #remain in login page
    else:
        return render(request, 'login.html')


def service(request):
    return render(request, 'service-details.html')

def starter (request):
    return render(request, 'starter-page.html')

def about (request):
    return render(request, 'about.html')

def myservice (request):
    return render(request, 'services.html')

def doctors (request):
    return render(request, 'doctors.html')


def appointment (request):
    if request.method == "POST":
        myappointment=Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            datetime=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message']
        )
        myappointment.save()
        return redirect('/show')

    else:
        return render(request, 'appointment.html')

def contact (request):
    if request.method == "POST":
        mycontact=Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        mycontact.save()
        return redirect('/showcontacts')
    else:
        return render(request, 'contact.html')

def show(request):
    allappointments = Appointment.objects.all()
    return render(request, 'show.html', {'appointment':allappointments})

def delete(request,id):
    appoint=Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('/show')

def showcontacts(request):
    allcontacts = Contact.objects.all()
    return render(request, 'showcontacts.html', {'contacts': allcontacts})


def deletecontact(request, id):
    print(f"Delete contact with ID: {id}")  # Check if the view is reached and ID is correct
    mycontact = get_object_or_404(Contact, id=id)
    mycontact.delete()
    return redirect('/showcontacts')

def edit(request,id):
    editappointment = Appointment.objects.get(id=id)
    return render(request, 'edit.html',{'appointment':editappointment})

def update(request,id):
    updateinfo = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html')

def register(request): #renders register and allows post values in database
    if request.method == "POST":
        members = Member( #the variable members is the container for storing the values
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password']
        )
        members.save()
        return redirect('/login') #takes you to the login form
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')