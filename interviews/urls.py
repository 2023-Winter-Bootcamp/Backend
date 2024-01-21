from django.urls import path
from .views import QuestionView, AnswerCreateView, InterviewResultView, InterviewListView, InterviewCreateView, \
    QuestionCreateView, InterviewProcessView

urlpatterns = [
    path('', InterviewListView.as_view(), name='interview-list-view'),
    path('<int:id>/', InterviewResultView.as_view(), name='interview-result-view'),
    path('<int:id>/questions/', QuestionView.as_view(), name='question-view'),
    path('questions/<int:id>/answers/create/', AnswerCreateView.as_view(), name='answer-create'),
    path('create/',InterviewCreateView.as_view(), name='interview-create'),
    path('<int:id>/questions/create/', QuestionCreateView.as_view(), name='question-create'),
    path('<int:interview_id>/questions/<int:question_id>/process/', InterviewProcessView.as_view(), name='interview-process'),

]
