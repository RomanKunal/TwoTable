from django.shortcuts import render

from .models import Doctor, Patient

def showDoc(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor.html', {'doctors': doctors})

def showPat(request):
    patients = Patient.objects.select_related('doctor').all()
    return render(request, 'patient.html', {'patients': patients})

