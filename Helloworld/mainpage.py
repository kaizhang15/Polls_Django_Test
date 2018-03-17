from django.http import HttpResponse
from django.shortcuts import render
 
def main_page(request):
    context          = {}
    return render(request, 'mainpage.html', context) 








