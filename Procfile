web: gunicorn helloworldjethro.wsgi --log-file -
# worker: celery -A helloworldjethro worker -B --loglevel=info
# worker: celery worker --app=counter.app  --loglevel=info
# worker: celery worker --app=helloworldjethro.app  --loglevel=info
worker: celery -A helloworldjethro worker
