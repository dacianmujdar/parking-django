web: gunicorn parking_project.wsgi --log-file -
worker: celery -A parking_project worker -E -B -l debug
