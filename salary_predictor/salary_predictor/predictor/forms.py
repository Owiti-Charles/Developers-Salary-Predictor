from django import forms

from .utilities import EdLevel, countries, dev_types, programming_languages, industries, platforms, remote_work

from .models import DeveloperSurvey


class SurveyForm(forms.ModelForm):

    programming_languages = forms.MultipleChoiceField(
        choices=programming_languages,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Programming Languages"
    )
    platforms = forms.MultipleChoiceField(
        choices=platforms,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Platforms"
    )

    def clean_years_code_pro(self):
        value = self.cleaned_data.get('years_code_pro')
        if value is not None and value < 0:
            raise forms.ValidationError("Years of professional coding must be non-negative.")
        return value



    def clean(self):
        cleaned_data = super().clean()
        years_code_pro = cleaned_data.get('years_code_pro')
        years_of_coding = cleaned_data.get('years_of_coding')
        # if years_code_pro and years_of_coding and years_code_pro > years_of_coding:
            # raise forms.ValidationError("Professional coding years cannot exceed total years coding.")
        return cleaned_data

    class Meta:
        model = DeveloperSurvey
        fields = [
            "dev_type",
            "years_code_pro",
            "years_of_coding",
            "ed_level",
            "countries",
            "programming_languages",
            "industry",
            "platforms",
            "remote_work",
        ]
        widgets = {
            "dev_type": forms.Select(
                choices=[("", "Select Developer Type"), *dev_types]
            ),
            "years_code_pro": forms.NumberInput(
                attrs={
                    "min": 0,
                    "step": 0.5,
                    "placeholder": "Years of professional coding",
                }
            ),
            "years_of_coding": forms.NumberInput(
                attrs={
                    "min": 0,
                    "step": 0.5,
                    "placeholder": "Total years coding (any context)",
                }
            ),
            "ed_level": forms.Select(
                choices=[("", "Select Education Level"), *EdLevel]
            ),
            "countries": forms.Select(choices=[("", "Select Country"), *countries]),
            "industry": forms.Select(
                choices=[("", "Select Industry"), *industries]
            ),
            "remote_work": forms.Select(
                choices=[("", "Select Remote Work"), *remote_work]
            ),

        }
