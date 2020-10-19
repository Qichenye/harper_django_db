from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.contrib.auth import authenticate
from rest_framework.views import APIView
import json
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# Create your views here.

class EntryView(APIView):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        # response = render(request, {})
        # response[WWW-Authenticate] = 'db'
        # print json raw
        # print(request.body)
        reqstring = request.body
        a = reqstring.find('email='.encode())
        aend = reqstring[a:].find('&'.encode())
        b = reqstring.find('password='.encode())
        bend = reqstring[b:].find('&'.encode())
        username = reqstring[a+6:aend]
        password = reqstring[b+9:bend]
        # print(username)
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # user = authenticate(username=body["username"], password=body["password"])
        user = authenticate(username=username, password=password)
        if user is not None:
            # TO DO: update last login field in database
            return HttpResponse(200)
        else:
            return HttpResponse(401)

    def get(self, request):
        list = Question.objects.order_by('-pub_date')[:5]
        context = {'list': list}
        return render(request, 'questions.html', context, status=200)

