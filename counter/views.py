from django.shortcuts import render
from .models import Counter

def counter_home(request):
    # increment counter here per visit and save it back into db
    # update or create
    # Counter.count += 1
    return render(request, 'counter/counter_home.html', {})
