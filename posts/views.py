from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from posts.models import Post
import random

# Create your views here.

def post_create(request):
	if request.user.is_authenticated():
		return HttpResponse("<H1>create</H1>")
	else:
		return HttpResponse("<H1>create2</H1>")

def post_detail(request , post_id):
	post = get_object_or_404(Post , id = post_id)
	context = {
		"post":post,
		"title":post.title,
	}
	return render(request, 'post_detail.html' , context)

def post_list(request):
	#Post.objects.create(title="auto post", content="created on page load")
	# if request.user.is_authenticated:
	queryset = Post.objects.all()
	# queryset = Post.objects.all()[:3]
	context = {
		'title' : "Posts",
		"posts" : queryset
	}

	return render(request, 'index.html', context)

def post_update(request):
	return HttpResponse("<H1>update</H1>")

def post_delete(request , post_id):
	Post.objects.filter(id = post_id).delete()
	return post_list(request)

def post_populate(request, pop_count):
	for i in range(int(pop_count)):
		title = random.randint(0,500)
		Post.objects.create(title=title, content="koukoubaounes"+str(title))
	return post_list(request)
