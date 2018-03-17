from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
#    return HttpResponse("Hello world ! ")

def html_test(request):
    context = {}
    return render(request, 'html_test.html', context)



