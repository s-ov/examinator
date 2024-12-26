from django import forms
from examinator.models.answer import Answer
from examinator.models.question import Question


class QuestionForm(forms.ModelForm):
    """Form for creating a question."""

    class Meta:
        model = Question
        fields = ['question_text', 'paper_test']
        labels = {
            'paper_test': 'Білет',
            'question_text': 'Запитання',
        }
        widgets = {
            'question_text': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Введіть питання...',
                }
            ),
            'paper_test': forms.Select(attrs={
                'class': 'form-control',
                }
            ),
        }

class AnswerForm(forms.ModelForm):
    """Form for creating a single answer."""

    class Meta:
        model = Answer
        fields = ['answer_text', 'is_correct']
        labels = {
            'answer_text': 'Відповідь',
            'is_correct': 'Чи правильна?',
        }
        widgets = {
            'answer_text': forms.TextInput(attrs={
                'placeholder': 'Введіть відповідь...',
                }
            ),
        }
        