from django.shortcuts import render

# Create your views here.
def principal(request):
    
    return(render (request,'index.html'))

def regcliente(request):
    
    return(render (request,'contacto_cliente.html'))
