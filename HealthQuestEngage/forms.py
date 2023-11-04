from django import forms
from .models import predictions


class predictionsForm(forms.ModelForm):
    class Meta:
        model = predictions
        fields = ['Name', 'Age', 'Weight', 'Height', 'BloodPressure','Cholesterol','ExerciseHours','Smoking','AlcoholConsumption','Diet','SleepHours','StressLevel']