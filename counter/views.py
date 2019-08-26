
import logging
from django.shortcuts import render
from .models import Counter

logger = logging.getLogger(__name__)

def counter_home(request):
    # increment counter here per visit and save it back into db
    # update or create
    # Counter.count += 1
    try:
        counter, created = Counter.objects.get_or_create(id=1)
        counter.visits += 1
        counter.save()
        logger.info('TESTING')
        logger.info('This page was visited %s times' % counter.visits)
        return render(request, 'counter/counter_home.html', {'visits': counter.visits })
    except Exception as e:
        logger.critical(e)
        return render(request, 'counter/counter_home.html', {'visits': 'ERROR' })
