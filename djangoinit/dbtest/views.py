from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    return HttpResponse(status=200)

def questions(request):
    list = Question.objects.order_by('-pub_date')[:5]
    context = {'list': list}
    return render(request, 'questions.html', context)