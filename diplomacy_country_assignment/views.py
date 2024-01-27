import numpy as np
from random import shuffle

from django.http import HttpResponse, HttpResponseRedirect
from django.forms import formset_factory
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from diplomacy_country_assignment.forms import AssignmentForm, COUNTRIES_CHOICES

# Create your views here.
def country_assign(formset):
    disallowed = {}
    for form in formset:
        disallowed[form.cleaned_data["player_name"]] = form.cleaned_data["countries"]
    
    # ensure all lists are same length
    max_games = np.max([len(val) for val in disallowed.values()])
    for player in disallowed:
        while len(disallowed[player]) < max_games:
            disallowed[player].append(None)
    
    countries = [key for key in COUNTRIES_CHOICES.keys()]
    player_names = list(disallowed.keys())
    shuffle(player_names)
    shuffle(countries)

    dis = np.array([disallowed[player] for player in player_names])
    samsies = np.sum([dis[:,i] == np.array(countries) for i in range(dis.shape[1])])
    attempts = 0

    while (np.sum(samsies) != 0) and (attempts < 100):
        #loop to make sure you haven't played that country before
        shuffle(player_names)
        shuffle(countries)
        dis = np.array([disallowed[player] for player in player_names])
        samsies = np.sum([dis[:,i] == np.array(countries) for i in range(dis.shape[1])])
        attempts += 1
        


    new_roles = {player:COUNTRIES_CHOICES[country] for player, country in zip(player_names,countries)}
    return new_roles

def assignment(request):
    AssignmentFormSet = formset_factory(AssignmentForm, min_num=7,extra=0)
    if request.method =="POST":
       
        
        formset = AssignmentFormSet(request.POST or None, request.FILES or None)
        
        if formset.is_valid():
            """
            do all the heavy lifting here. Probably not how it's supposed
            to work but I don't care.
            """
            new_roles = country_assign(formset)
            return render(request,
                'diplomacy_country_assignment/success.html',
                {"new_roles" : new_roles}
                )
    
    else:
        formset = AssignmentFormSet()
    
    context = {"formset": formset,
               }
    return render(request,
                  "diplomacy_country_assignment/assignment.html",
                  context )

def success(request):
    return render(request, "diplomacy_country_assignment/success.html", {})