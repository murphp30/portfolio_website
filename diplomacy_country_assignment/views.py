import numpy as np
from random import shuffle

from django.core.mail import send_mass_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import formset_factory
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from diplomacy_country_assignment.forms import AssignmentForm, COUNTRIES_CHOICES

# Create your views here.
def country_assign(formset):
    """
    Assign countries by shuffling until a new configuration is reached.
    TODO: Figure out how to handle emails securely and protect against spam.
    """
    disallowed = {}
    # player_emails = {}
    for form in formset:
        disallowed[form.cleaned_data["player_name"]] = form.cleaned_data["countries"]
        # player_emails[form.cleaned_data["player_name"]] = form.cleaned_data["player_email"]
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
        # loop to make sure you haven't played that country before
        shuffle(player_names)
        shuffle(countries)
        dis = np.array([disallowed[player] for player in player_names])
        samsies = np.sum([dis[:,i] == np.array(countries) for i in range(dis.shape[1])])
        attempts += 1
        


    new_roles = {player:COUNTRIES_CHOICES[country] for player, country in zip(player_names,countries)}
    # messages = []
    # for player in new_roles:
    #     messages.append(email_players(player, player_emails[player], new_roles[player]))
    # messages = tuple(messages)
    # send_mass_mail(messages, fail_silently=False)
    return new_roles

def email_players(name, email, country):
    #send email to all players. Takes player name, player email and player country
    # sender_email="" #sender email
    to = [email]
    subject = "Diplomacy Times January 1901"
    text = "Europe on the brink of war!\nAs relations between " +\
    country +\
    " and their neighbours deteriorates, it is up to " +\
    name +\
    " to take the nation's helm and lead them through the darkest hours the continent has faced in centuries.\n" +\
    """Hello, """ + name + """. For this game of Diplomacy you will be playing as """ + country +\
    """.\nGood luck and have fun!"""

    message = (subject, text, None, to)
    return message

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
                {"new_roles" : new_roles,
                 "formset":formset}
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