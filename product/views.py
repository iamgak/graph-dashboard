from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
# from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required

attributes = ['end_year', 'intensity', 'sector', 'topic', 'insight', 'url', 'region', 'start_year', 'impact', 'added', 'published', 'country', 'relevance', 'pestle', 'source', 'title', 'likelihood']


def dash(request):
    
    if request.user.is_authenticated == False:
        return redirect('login')
    
    data1 = Dashboard.objects.all()[:5]
    if request.method == "GET" and len(request.GET) == 2:
        first = request.GET["first"]
        second = request.GET["second"]
        if first and second:
            filter_dict ={first:second}
            data1 = Dashboard.objects.all().filter(**filter_dict)[:5]
    loop_times = range(1,len(data1))
    response = render(request, 'dash1.html',{'data':data1,"loop_times":loop_times,'attributes':attributes})
    # response.delete_cookie('message')
    return response

# def login(request):

#     data = {'message': 'Hello from the server!'}
#     return JsonResponse(data)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dash')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        # print(user)
        messages.success(request,'')
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            # return redirect('dash')
            # response = render(request, 'dash.html')
            # response.delete_cookie('message')
            return redirect('dash')  
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, '')
    return redirect('login')