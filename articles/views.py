from django.shortcuts import render
from .forms import ArticlesForm
from .models import Articles

def post(request):
    form = ArticlesForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data = form.cleaned_data
        article = Articles.objects.create(title = data["title"], body = data["body"])
        article.save()
        print (article)

    return render(request, "articles/post.html", locals())

def posts(request):
    result = Articles.objects.all().order_by("-date").values()[:20]
    print(Articles.objects.values())
    print(result)
    return render (request, "articles/posts.html", {'articles': result})
