from django.urls import path
from .views import (
    home_view, 
    create_question_view, 
    list_question_view, 
    get_question_answers_view,
    )


app_name = 'examinator'

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_question_view, name='create_question'),
    # path('create/<int:question_id>', create_question_view, name='create_question'),
    path('list_question/', list_question_view, name='list_question'),
    path('question_answers/<int:question_id>', get_question_answers_view, name='question_answers'),
]