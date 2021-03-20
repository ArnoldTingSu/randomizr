from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['random_word'] = get_random_string(length=14)
    request.session['count'] += 1
    return render(request, 'random.html')

def reset(request):
    request.session['count'] = 0
    return render(request,'random.html')