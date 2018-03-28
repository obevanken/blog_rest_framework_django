from django.shortcuts import render, redirect
from .forms import ArticlesForm
from django.contrib.auth.models import User
from .models import Articles

def create(request):
    if request.user.is_authenticated:
        form = ArticlesForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            print (request.POST)
            print(request.user.id)
            print (form.cleaned_data)
            data = form.cleaned_data
            article = Articles.objects.create(title = data["title"], body = data["body"], user = request.user)
            article.save()
            print (article)
            return redirect('/')
        return render(request, "articles/create.html", locals())
    else:
        return redirect('/login')



def posts(request):
    if request.user.is_authenticated:
        result = Articles.objects.select_related().order_by("-date")[:20]
        users = User.objects.all().prefetch_related("user")
        print(result)
        return render(request, "articles/posts.html", {'articles': result})
    else:
        return redirect('/login')

def post(request, pk):
    if request.user.is_authenticated:
        article = Articles.objects.select_related().filter(id = pk)
        print(article)
        return render(request, "articles/post.html",{'article':article} )
    else:
        return redirect('/login')
