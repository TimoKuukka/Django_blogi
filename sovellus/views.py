from django.shortcuts import render

# Create your views here.

def postaukset(request):
    return render(request, "blogi/postauslista.html")
