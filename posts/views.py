from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from posts.models import Post
from .forms import PostForm
import random

def post_create(request):
	# if request.method == "POST":
	# 	title = request.POST['title']
	# 	content = request.POST['content']
	# 	Post.objects.create(title = title, content = content)
	# 	return post_list(request)

	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return post_list(request)

	context = {
		"form":form,
	}
	return render(request, "post_form.html" , context)
	

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