from django.http import HttpResponse, HttpResponseRedirect
# from django.forms import formset_factory
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from diplomacy_country_assignment.forms import AssignmentFormSet

# Create your views here.
def assignment(request):
    # AssignmentFormSet = formset_factory(AssignmentForm, extra=2)
    if request.method =="POST":
        formset = AssignmentFormSet(request.POST)
        
        if formset.is_valid():
            return HttpResponseRedirect(
                reverse('diplomacy_country_assignment_success')
                )
    
    else:
        formset = AssignmentFormSet()
    
    context = {"formset": formset,
              }
    return render(request,
                  "diplomacy_country_assignment/assignment.html",
                  context )