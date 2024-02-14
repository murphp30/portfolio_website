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
    error_css_class = "error"
    required_css_class = "required"
    player_name = forms.CharField(max_length=20,
                                  required=True,
                                  error_messages={"required": "Please enter player name"})
    player_email = forms.EmailField(required=True,
                                    help_text="Required. Will email the player with their assigned country.",
                                    error_messages={"required": "Please enter player email."})
    countries = forms.MultipleChoiceField(
        required=False,
        widget=HorizWidget,
        choices=COUNTRIES_CHOICES,
        help_text="Check box if player has already played as that country."
    )
    def clean_player_name(self):
        player_name = self.cleaned_data["player_name"]
        return player_name
    def clean_player_email(self):
        player_email = self.cleaned_data["player_email"]
        return player_email