from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import F
from django.urls import reverse
from django.utils import timezone

from .models import Choice, Question


# create your views here.
# note: the redundancy can be removed switching to the generic-view model
def index(request):
    questions = Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    return render(request, "polls/index.html", {"questions": questions})

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question with that ID does not exist")
    
    # the above code is the long form of get_object_or_404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # F is used to avoid race conditions
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        
        # always return an HttpResponseRedirect after successfully submitting data using POST
        # this prevents data from being posted twice if the user hits the Back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
