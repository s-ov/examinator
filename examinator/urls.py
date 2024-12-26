from django.urls import path
from .views import (
    home_view, 
    create_question_view, 
    list_question_view, 
    get_question_answers_view,

    TestPaperCreateView,
    TestPaperListView,
    TestPaperDetailView,

    KnowledgeTestCreateView,
    KnowledgeTestListView,
    KnowledgeTestDetailView,
    )


app_name = 'examinator'

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_question_view, name='create_question'),
    # path('create/<int:question_id>', create_question_view, name='create_question'),
    path('list_question/', list_question_view, name='list_question'),
    path(
        'question_answers/<int:question_id>', 
        get_question_answers_view, 
        name='question_answers',
        ),

    path(
        'testpaper_create/', 
        TestPaperCreateView.as_view(), 
        name='testpaper_create',
        ),
    path(
        'testpaper_list/', 
        TestPaperListView.as_view(), 
        name='testpaper_list',
        ),
    path(
        'testpaper_detail/<slug:slug>', 
        TestPaperDetailView.as_view(), 
        name='testpaper_detail',
        ),

    path(
        'knowledge_test_create/', 
        KnowledgeTestCreateView.as_view(), 
        name='knowledge_test_create',
        ),
    path(
        'knowledge_test_list/', 
        KnowledgeTestListView.as_view(), 
        name='knowledge_test_list',
        ),
    path(
        'knowledge_test_detail/<slug:slug>', 
        KnowledgeTestDetailView.as_view(), 
        name='knowledge_test_detail',
        ),
]