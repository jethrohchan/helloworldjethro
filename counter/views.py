from django.shortcuts import render
from .models import Counter

def counter_home(request):
    # increment counter here per visit and save it back into db
    # update or create
    # Counter.count += 1
    counter, created = Counter.objects.get_or_create(id=1)
    counter.visits += 1
    counter.save()
    return render(request, 'counter/counter_home.html', {'visits': counter.visits })