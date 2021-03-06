
import logging
from django.shortcuts import render
from .models import Counter
from django.conf import settings
from .tasks import increment

logger = logging.getLogger(__name__)

def counter_home(request):
    # entrypoint
    try:
        increment.delay()
        counter, created = Counter.objects.get_or_create(id=1)
        return render(request, 'counter/counter_home.html', {'visits': counter.visits, 'runtimes': counter.runtimes })
    except Exception as e:
        logger.critical(e)
        return render(request, 'counter/counter_home.html', {'visits': 'ERROR', 'runtimes': 'ERROR' })
