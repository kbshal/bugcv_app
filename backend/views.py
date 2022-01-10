from django.shortcuts import render,redirect
from django.urls import path,include
from django.http import Http404,HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def endpoints(request):
    routes=[
        {
            "Endpoint":"/test",
            "method":"GET",
            "body":None,
            "description":"This is a test file"
        }
    ]
    return Response(routes)
