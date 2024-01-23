from django import forms
from django.forms import formset_factory

COUNTRIES_CHOICES = {
    "britain": "Britain",
    "france": "France",
    "germany": "Germany",
    "austria": "Austria",
    "italy": "Italy",
    "russia": "Russia",
    "turkey": "Turkey"
}

class AssignmentForm(forms.Form):
    player_name = forms.CharField(max_length=20)
    player_email = forms.EmailField(required=False)
    # countries = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=COUNTRIES_CHOICES,
    # )
    britain = forms.BooleanField(required=False)
    france = forms.BooleanField(required=False)
    germany = forms.BooleanField(required=False)
    austria = forms.BooleanField(required=False)
    italy = forms.BooleanField(required=False)
    russia = forms.BooleanField(required=False)
    turkey = forms.BooleanField(required=False)
    def clean_player_name(self):
        player_name = self.cleaned_data["player_name"]
        return player_name
    def clean_player_email(self):
        player_email = self.cleaned_data["player_email"]
        return player_email

AssignmentFormSet = formset_factory(AssignmentForm, min_num=7,extra=0)