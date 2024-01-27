from django.test import TestCase
from django.forms import formset_factory

from diplomacy_country_assignment.forms import AssignmentForm, COUNTRIES_CHOICES
from diplomacy_country_assignment.views import country_assign
# Create your tests here.
class FormTests(TestCase):
    def test_not_assigned_previous_country(self):
        """
        Test that a player is not assigned a country
        they've already played as.
        """
        disallowed = {
            "player1": ["britain"],
            "player2": [],
            "player3": [],
            "player4": [],
            "player5": [],
            "player6": [],
            "player7": [],
        }
        AssignmentFormSet = formset_factory(AssignmentForm, min_num=7,extra=0)
        data = {"form-TOTAL_FORMS": "7", "form-INITIAL_FORMS": "0"}
        for i, player in enumerate(disallowed):
            data["form-{}-player_name".format(i)] = player
            data["form-{}-countries".format(i)] = disallowed[player]
            
        formset = AssignmentFormSet(data)
        if formset.is_valid():
            new_roles = country_assign(formset)
        
        self.assertIs(new_roles["player1"] == "Britain", False)

    def test_unique_countries(self):
        return