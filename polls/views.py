from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice
from django.template import loader
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name ='polls/results.html'

def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
#    output = ', '.join([q.question_text for q in latest_question_list])
    context = {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context, request))
#    return HttpResponse(output)
#    return render(request, 'polls/index.html', context) 


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
#    return HttpResponse("You're looking at question %s." % question_id)
#from django.shortcuts import get_object_or_404

#    The function get_object_or_404 can handle this situation successfully!
#    get_list_or_404 is used when need to filter a list.

#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#    return HttpResponse("You're voting on question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})




# Create your views here.
