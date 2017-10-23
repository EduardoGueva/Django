from django.shortcuts import render

# Create your views here.

from .models import Post

#Vista para el read
def index(request):
	context={
	'posts':Post.objects.all().order_by('-id')
	}
	return render(request,'index.html',context)

#Vista para el create
def add(request):
#	if request.method=='POST':
		#agrega formulario
#		form=PostForm(request.POST)
#		if form.is_valid():
#			return HttpResponseRedirect(reverse('post_index'))
#	else: 
		#muestralo
#		form=PostForm()
#		context={'form':form}
	post=Post(title=request.POST['Title'],body=request.POST['Body'])
	post.save();
	return render(request,'add.html')

def update(request):
	Post.objects.all.update();
	return render(request,'update.html')

