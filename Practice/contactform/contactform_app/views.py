from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Empdata
from .forms import Empform


def contactform_view(request):
    if request.method == "POST":
        eform = Empform(request.POST)
        if eform.is_valid():
            name = request.POST.get('name')
            salary = request.POST.get('salary')
            email = request.POST.get('email')
            location = request.POST.get('location')

            data = Empdata(
                name=name,
                salary=salary,
                email=email,
                location=location
            )
            data.save()
            eform = Empform()
            return render(request, 'contactform.html', {'eform': eform})
        else:
            return HttpResponse('Invalid Data')
    else:
        eform = Empform()
        return render(request, 'contactform.html', {'eform': eform})


def contactform_display(request):
    edata = Empdata.objects.all()
    return render(request, 'contactform_display.html', {'edata': edata})
