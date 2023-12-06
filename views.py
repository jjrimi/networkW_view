from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from polls.models import Question, Choice
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)


def voet(request, question_id):
    logger.debug(f"vote().question_id: {question_id}")
    question = get_object_or_404(Question, pk=question_id)

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        """
        return the last five published questions.
        """
        return Question.objects.order_by('-pub_date')[:5]


class vote(DetailView):
    model = Question
    template_name = 'polls/vote.html'

    def get_object(self, queryset=None):
        """
        Returns the object the view is displaying.

        This is overridden to get the object by the primary key (`pk`) from the URL.
        """
        question_id = self.kwargs.get('question_id', None)
        return get_object_or_404(Question, pk=question_id)


class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'

class Detailview(DetailView):
    model = Question
    template_name = 'polls/detail.html'
