from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
    }

    if request.method == 'POST':
        context['nama'] = request.POST['nama']
        context['address'] = request.POST['address']

    return render(request, 'index.html', context)