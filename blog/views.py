from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages as message
from .models import Post
from .forms import FormPost, FormPostDelete

# Create your views here.
def index(request):
	data = Post.published.all()
	return render(request, 'blog/post/index.html', {'data': data})

def post_add(request):
	if request.method == 'POST':
		form = FormPost(request.POST)
		if form.is_valid():
			form.save()
			message.success(request, 'Berhasil')
			return HttpResponseRedirect(reverse('blog:blog_index'))
	else:
		form = FormPost()
	return render(request, 'blog/post/post_add.html', {'form':form})

def post_detail(request, pk):

	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post/post_detail.html',{'post': post})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		form = FormPost(data=request.POST,instance=post)
		if form.is_valid():
			form.save()
			message.success(request, 'Berhasil')
			return HttpResponseRedirect(reverse('blog:blog_index'))
	else:
		form = FormPost(instance=post)
	return render(request, 'blog/post/post_add.html',{'post': post,'form': form})

def post_delete(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		form = FormPostDelete(data=request.POST,instance=post)
		if form.is_valid():
			post.delete()
			message.success(request, 'Berhasil')
			return HttpResponseRedirect(reverse('blog:blog_index'))
	else:
		form = FormPostDelete(instance=post)
	return render(request, 'blog/post/post_delete_confirm.html',{'post': post,'form': form})




def coeg(request):
	return HttpResponse('hello it"s me coeg')

