from django.shortcuts import render

# Create your views here.

#view de página de inicio por función:
def indexView(request):
    return render(request, 'index.html', {})
