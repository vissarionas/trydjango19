from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_create(request):
	return HttpResponse("<H1>create</H1>")

def post_detail(request):
	return HttpResponse("<H1>detail</H1>")

def post_list(request):
	return HttpResponse("<H1>list</H1>")

def post_update(request):
	return HttpResponse("<H1>update</H1>")

def post_delete(request):
	return HttpResponse("<H1>delete</H1>")

