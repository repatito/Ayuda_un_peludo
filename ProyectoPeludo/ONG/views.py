from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"../templates/index.html")

def gatos(request):
    return render(request,"../templates/gatos.html")

def humberta(request):
        return render(request,"../templates/humberta.html")
def chuchito(request):
        return render(request,"../templates/chuchito.html")
def blanquita(request):
        return render(request,"../templates/blanquita.html")

def perros(request):
    return render(request,"../templates/perros.html")
def luchito(request):
        return render(request,"../templates/luchito.html")
def bizcochito(request):
        return render(request,"../templates/bizcochito.html")
def chocolate(request):
        return render(request,"../templates/chocolate.html")