from django.shortcuts import render
from messenger.models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def index(request):
	return render(request, 'messenger/index.html')



 	return render(request, 'messenger/index.html', {'instance': instance})


def detail(request, slug):
	instance = Post.objects.filter(slug=slug)
	return render(request, 'messenger/detail.html', {'instance': instance})


	return render(request, 'messenger/register.html', context)


@login_required(login_url='/account/login/')
def post_new(request):
	instance = Post.objects.all()
	form = PostForm(request.POST or None)
	if form.is_valid():
		info = form.save(commit=False)
		info.user = request.user
		info.save()
	 	return render(request, 'messenger/index.html', {'instance': instance})
	return render(request, 'messenger/post.html', {'form':form})

def discover(request):
	instance = Post.objects.all()
	return render(request, 'messenger/discover.html', {'instance': instance})


