from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.core import serializers

from .models import Choice, Question
import json


class IndexView(generic.ListView):
    template_name = 'chart/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class jsView(generic.ListView):
    model = Question    
    template_name = 'chart/js.html'


class DetailView(generic.DetailView):
    model = Question
    template_name = 'chart/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'chart/results.html'

def get_dots(request):
    points = [{"model": "charts.daten", "pk": 5, "fields": {"Br": 2.0, "Pumpentyp": "GP   -200M/  4x440", "Qn": 600.0, "Drehzahl": 2980.0, "Lrd": 427.0, "NWDS": 50.0, "NWSS": 100.0, "Pn": 16.0, "B": 0.0, "M": 0.0, "V": 0.0, "H1": 1108.4093908977954, "Q1": 0.0, "H2": 1103.4615359830075, "Q2": 141.18, "H3": 1077.7130176600456, "Q3": 317.65, "H4": 987.6412656143883, "Q4": 494.12, "H5": 962.2829325176394, "Q5": 529.41, "H6": 934.7088858982681, "Q6": 564.71, "H7": 767.3681793889864, "Q7": 741.15}}, {"model": "charts.daten", "pk": 5, "fields": {"Br": 2.0, "Pumpentyp": "GP   -200M/  4x440", "Qn": 600.0, "Drehzahl": 2980.0, "Lrd": 427.0, "NWDS": 50.0, "NWSS": 100.0, "Pn": 16.0, "B": 0.0, "M": 0.0, "V": 0.0, "H1": 1108.4093908977954, "Q1": 0.0, "H2": 1103.4615359830075, "Q2": 141.18, "H3": 1077.7130176600456, "Q3": 317.65, "H4": 987.6412656143883, "Q4": 494.12, "H5": 962.2829325176394, "Q5": 529.41, "H6": 934.7088858982681, "Q6": 564.71, "H7": 767.3681793889864, "Q7": 741.15}}, {"model": "charts.daten", "pk": 4, "fields": {"Br": 2.0, "Pumpentyp": "GP   -200M/  3x440", "Qn": 600.0, "Drehzahl": 2980.0, "Lrd": 427.0, "NWDS": 50.0, "NWSS": 100.0, "Pn": 16.0, "B": 0.0, "M": 0.0, "V": 0.0, "H1": 831.3070431733466, "Q1": 0.0, "H2": 827.5961519872554, "Q2": 141.18, "H3": 808.284763245034, "Q3": 317.65, "H4": 740.7309492107912, "Q4": 494.12, "H5": 721.7121993882295, "Q5": 529.41, "H6": 701.031664423701, "Q6": 564.71, "H7": 575.5261345417398, "Q7": 741.15}}, {"model": "charts.daten", "pk": 1, "fields": {"Br": 2.0, "Pumpentyp": "GP_D -200L/ 11x440", "Qn": 480.0, "Drehzahl": 2980.0, "Lrd": 412.0, "NWDS": 50.0, "NWSS": 100.0, "Pn": 16.0, "B": 0.0, "M": 0.0, "V": 0.0, "H1": 2977.606516734797, "Q1": 0.0, "H2": 2973.7719556257175, "Q2": 96.0, "H3": 2905.777760075604, "Q3": 256.0, "H4": 2611.903591309814, "Q4": 416.0, "H5": 2532.1789234602384, "Q5": 448.0, "H6": 2445.3791454217435, "Q6": 480.0, "H7": 1892.6161200437662, "Q7": 640.0}}]
    data = json.dumps(points)
    return HttpResponse(data, content_type="application/json")

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'chart/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('chart:results', args=(question.id,)))