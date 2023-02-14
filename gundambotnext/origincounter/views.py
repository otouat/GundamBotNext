from django.shortcuts import render

def index(request):
    return render(request=request, template_name='origincounter/index.html')

def contact(request):
    return render(request, 'origincounter/contact.html')