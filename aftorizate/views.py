# from django.shortcuts import render, redirect
# from .forms import RegisterForm
# from .serializers import UserSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages


# @api_view(['GET', 'POST'])
# def register(request):
#     if request.method == "GET":
#         users = User.objects.all()
#         serializer = UserSerializer(users, many = True)
#         return Response(serializer.data)
#     # form = RegisterForm(request.POST or None)
#     elif request.method == "POST":
#         result = authenticate(username=request.POST['username'], password=request.POST['password'])
#         print(request.POST.username)
#         serializer = UserSerializer(data = request.data)
#         if result is not None:
#             print('none')
#             messages.debug(request, ' Username alredy use.')
#         else:
#
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             # print("зашел")
#             # user = User.objects.create_user(data['username'], data['email'], data['password'])
#             # user.save()
#             # print(user)
#             # return redirect('/')
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     # return render(request, "auth/register.html", locals())
#
#
# @api_view(['GET', 'POST'])
# def login_auth(request):
#     if request.method == "GET":
#         users = User.objects.all()
#         serializer = UserSerializer(users, many = True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         print(user)
#         if user is not None:
#                 serializer = UserSerializer(data = request.data)
#                 if serializer.is_valid():
#                     return Response(serializer.data, status=status.HTTP_201_CREATED)
#                     login(request, user)
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# def logout_auth(request):
#     logout(request)
#     return redirect("/login")
