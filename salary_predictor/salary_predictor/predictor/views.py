from django.shortcuts import render

from .utilities import predict_salary
from .forms import SurveyForm

# Create your views here.


def home(request):
    """Render the home page with the survey form."""
    prediction = None
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            prediction = predict_salary(data)
            print(f"Prediction: {prediction}")
    else:
        form = SurveyForm()

    return render(request, "home.html", {'form': form, 'prediction': prediction})
