from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from personality_test.models import Choice, Question

# Create your views here.
def index(request):
    context = {}
    return render(request, "personality_test/index.html", context )

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 
                  "personality_test/detail.html", 
                  {"question":question})

def results(request):
    questions = Question.objects.all()
    character_tally = {
        "Tommy Shlug":0,
        "Francis 'The Viper' Higgins":0,
        "Fontaine":0,
        "Conor Williams":0,
        "The Purple Onion":0,
        "John's father":0
    }
    character_blurb = {
        "Tommy Shlug": "You're some man for one man. Be careful driving \
                        the bus for NATO.",
        "Francis 'The Viper' Higgins": "From the mean streets of Castletown \
                                        to an internet media mogul.",
        "Fontaine": "I'm here to inform you, you got a son!",
        "Conor Williams": "You have a mysterious past but that's ok \
                           because you can drive away from it in the new \
                           Mercedes E class.",
        "The Purple Onion": "A senior ticket for yourself is it? \
                             You enjoy the simpler thhings in life, \
                             like riding the bus ten times a day.",
        "John's father": "A great man, gone! \
                          You should Zurich it up incase you meet a similar \
                          fate on the mighty Eiger."
    }
    for q in questions:
        choices = q.choice_set.all()
        for c in choices:
            character_tally[c.character_name] += c.votes
            # must be a better way to reset each time
            c.votes = 0
            c.save()
    max_character = max(character_tally, key=character_tally.get)
    
    return render(request, 
                  "personality_test/results.html", 
                  {"character":max_character,
                   "blurb": character_blurb[max_character]})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "personality_test/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        if question.id < Question.objects.count():
            return HttpResponseRedirect(reverse("personality_test:detail",
                                                args=(question.id + 1,)))
        else:
            
            return HttpResponseRedirect(reverse("personality_test:results"))