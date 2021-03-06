from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse
from .models import Question, Choice

# Create your views here.
#

def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html', context)

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/results.html',{'question':question})

def vote(request,question_id):
    p = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.post['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':p,
            'error_message':"你不能选择这个。",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponsePermanentRedirect(reverse('polls:results', args=(p.id,)))