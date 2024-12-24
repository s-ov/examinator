from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.urls import reverse_lazy
from django import forms
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from examinator.models.answer import Answer
from examinator.models.question import Question
from examinator.models.test_paper import TestPaper
from examinator.models.knowledge_test import KnowledgeTest
from .forms import QuestionForm, AnswerForm


def home_view(request):
    """Render the home page."""
    
    return render(request, 'examinator/base_examinator.html',)


def create_question_view(request):
    """View to create a question and its answers."""
    AnswerFormSet = modelformset_factory(Answer, form=AnswerForm, extra=5, can_delete=True)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        answer_formset = AnswerFormSet(request.POST, queryset=Answer.objects.none())

        if question_form.is_valid() and answer_formset.is_valid():
            question = question_form.save()

            for answer_form in answer_formset:
                if answer_form.cleaned_data and not answer_form.cleaned_data.get('DELETE'):
                    answer = answer_form.save(commit=False)
                    answer.question = question
                    answer.save()

            return redirect('examinator:home')  

    else:
        question_form = QuestionForm()
        answer_formset = AnswerFormSet(queryset=Answer.objects.none())

    return render(
        request,
        'examinator/create_question.html',
        {
            'question_form': question_form,
            'answer_formset': answer_formset,
            'title': 'Створити запитання та можливі відповіді'
        },
    )


def list_question_view(request):
    """View to list all questions."""
   
    questions = Question.objects.all()
    context = {
        'questions': questions,
        'title': 'Список запитань',
    }

    return render(
        request, 
        'examinator/question_list.html', 
        context,
        )   

def get_question_answers_view(request, question_id):
    question = Question.objects.get(pk=question_id)
    answers = question.answers.all()
    context = {
        'question': question,
        'answers': answers,
        'title': 'Відповіді на запитання',
    }

    return render(
        request, 
        'examinator/question_answers.html', 
        context,
        )


class TestPaperCreateView(CreateView):
    "View to create a new test paper instance."
    model = TestPaper
    fields = ['ordinal_number', 'slug', 'knowledge_test']  
    template_name = 'examinator/test_paper_form.html'  
    success_url = reverse_lazy('examinator:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Сформувати білет'
        return context


class TestPaperListView(ListView):
    "View to list all test paper instances."
    def get(self, request):
        test_papers = TestPaper.objects.all()
        context = {
            'test_papers': test_papers,
            'title': 'Список білетів',
        }
        return render(request, 'examinator/test_paper_list.html', context)


class TestPaperDetailView(DetailView):
    model = TestPaper
    template_name = 'examinator/test_paper_detail.html' 
    context_object_name = 'test_paper'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Деталі білета'
        return context


class KnowledgeTestCreateView(CreateView):
    "View to create a new knowledge test instance."
    model = KnowledgeTest
    fields = ['title', 'slug']  
    template_name = 'examinator/knowledge_test_form.html'  
    success_url = reverse_lazy('examinator:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Створити тест'
        return context
