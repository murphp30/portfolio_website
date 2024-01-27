from django import forms

COUNTRIES_CHOICES = {
    "britain": "Britain",
    "france": "France",
    "germany": "Germany",
    "austria": "Austria",
    "italy": "Italy",
    "russia": "Russia",
    "turkey": "Turkey"
}

from django.utils.safestring import mark_safe

class HorizWidget(forms.CheckboxSelectMultiple):

    def render(self, *args, **kwargs):
        output = super(HorizWidget, self).render(*args,**kwargs) 
        return mark_safe(output.replace(u'</div><div>', u''))
    
class AssignmentForm(forms.Form):
    player_name = forms.CharField(max_length=20, required=True)
    player_email = forms.EmailField(widget=forms.HiddenInput(),required=False)
    countries = forms.MultipleChoiceField(
        required=False,
        widget=HorizWidget,
        choices=COUNTRIES_CHOICES,
    )
    # britain = forms.BooleanField(required=False)
    # france = forms.BooleanField(required=False)
    # germany = forms.BooleanField(required=False)
    # austria = forms.BooleanField(required=False)
    # italy = forms.BooleanField(required=False)
    # russia = forms.BooleanField(required=False)
    # turkey = forms.BooleanField(required=False)
    def clean_player_name(self):
        player_name = self.cleaned_data["player_name"]
        return player_name
    def clean_player_email(self):
        player_email = self.cleaned_data["player_email"]
        return player_email

