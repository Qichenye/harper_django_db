from django.urls import path
from .views import EntryView

urlpatterns = [
    path('', EntryView.as_view())
    #path('', views.index, name='index'),
    #path('questions', views.questions, name='questions')
]
