from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from posts.models import Post
from .forms import PostForm
from django.contrib import messages

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "new post created")
		return HttpResponseRedirect(instance.get_absolute_url())

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
	queryset = Post.objects.all()
	context = {
		'title' : "Posts",
		"posts" : queryset
	}

	return render(request, 'index.html', context)

def post_update(request , post_id=None):
	instance = get_object_or_404(Post, id = post_id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context ={
		"form":form,
		"title":instance.title,
	}
	return render(request, "post_form.html" , context)


def post_delete(request , post_id):
	Post.objects.filter(id = post_id).delete()
	return redirect('posts:posts')