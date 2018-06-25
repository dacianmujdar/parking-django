web: gunicorn parking_project.wsgi
worker: celery -A parking_project worker -E -B -l debug
