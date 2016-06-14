from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_create(request):
	if request.user.is_authenticated():
		return HttpResponse("<H1>create</H1>")
	else:
		return HttpResponse("<H1>create2</H1>")

def post_detail(request):
	return HttpResponse("<H1>detail</H1>")

def post_list(request):
	context = {
	"title":"goofy_list",
	}
	#return HttpResponse("<H1>list</H1>")
	return render(request, 'index.html' , context)

def post_update(request):
	return HttpResponse("<H1>update</H1>")

def post_delete(request):
	return HttpResponse("<H1>delete</H1>")

