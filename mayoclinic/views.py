from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from lab.models import Lab


def homepage(request):
    labData=Lab.objects.all();
    data={
        'labData':labData

        # 'MayoClinicLaboratories':'Home Page',
    }
    return render(request,"algorithms.html",data)
def labDetails(request,labid):
    labDetails=Lab.objects.get(id=labid)
    data={
        'labDetails':labDetails
    }
    return render(request,"algorithms.html",data)


def mayoAlgo(request):
    return HttpResponse("Welcome to Mayo Clinic Laboratories")

