# from django.http import HttpResponse, JsonResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from .models import Articles
# from .serializers import ArticlesSerializer
#
# def create(request):
#     if request.user.is_authenticated:
#         form = ArticlesForm(request.POST or None)
#         if request.method == "POST" and form.is_valid():
#             print (request.POST)
#             print(request.user.id)
#             print (form.cleaned_data)
#             data = form.cleaned_data
#             article = Articles.objects.create(title = data["title"], body = data["body"], user = request.user)
#             article.save()
#             print (article)
#             return redirect('/')
#         return render(request, "articles/create.html", locals())
#     else:
#         return redirect('/login')
#
#
# @api_view(['GET', 'POST'])
# def posts(request):
#     if request.user.is_authenticated:
#         result = Articles.objects.select_related().order_by("-date")[:20]
#         serializer = ArticlesSerializer(result, many=True)
#         users = User.objects.all().prefetch_related("user")
#         return Response(serializer.data)
#     else:
#         return redirect('/login')
#
# @api_view(['GET', 'POST'])
# def post(request, pk):
#     if request.user.is_authenticated:
#         article = Articles.objects.prefetch_related().get(id = pk)
#         serializer = ArticlesSerializer(article)
#         return Response(serializer.data)
#     else:
#         return redirect('/login')
