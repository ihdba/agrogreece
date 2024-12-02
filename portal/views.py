from django.shortcuts import render

# Create your views here.



def index(request):
    
    title = 'Εισαγωγη'
    ctx = {
        'title': title,
    }
    
    return render(request, 'portal/index.html', ctx)


def about(request):
    
    title = 'Ποιο ειμαστε'
    ctx = {
        'title': title,
    }
    
    return render(request, 'portal/about.html', ctx)


def contact(request):
    title = 'Επαφη'
    ctx = {
        'title': title,
    }
    
    return render(request, 'portal/contact.html', ctx)