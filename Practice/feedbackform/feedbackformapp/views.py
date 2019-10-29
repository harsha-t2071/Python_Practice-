from django.http.response import HttpResponse
from django.shortcuts import render
from .models import FeedbackData
from .forms import FeedbackForm
import datetime as dt

date = dt.datetime.now()


def feedback_view(request):
    if request.method == 'POST':
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')

            data = FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date
                )
            data.save()
            fform = FeedbackForm()
            fdata = FeedbackData.objects.all()
            return render(request, "feedback.html", {'fform': fform, 'fdata': fdata})
        else:
            return HttpResponse("User Entered Invalid Data")
    else:
        fform = FeedbackForm(request.POST)
        fdata = FeedbackData.objects.all()
        return render(request, 'feedback.html', {'fform': fform, 'fdata': fdata})

