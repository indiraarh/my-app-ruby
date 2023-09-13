from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Indira Arifia Rahmah',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)

def index(request):
    template = "main/main.html"
    return render(request, template)
