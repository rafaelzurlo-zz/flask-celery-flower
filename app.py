from flask import Flask
from celery import Celery
from datetime import timedelta
import time
import os

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL=f"redis://:{os.environ.get('REDIS_PASSWORD')}@redis:6379/0",
    CELERY_RESULT_BACKEND=f"redis://:{os.environ.get('REDIS_PASSWORD')}@redis:6379/0"
)
celery = make_celery(app)

@celery.task()
def execute_worker(message):
    print("Executing")
    print(message)
    time.sleep(60)
    return True

@app.route('/message')
def print_message():
    result = execute_worker.delay("My message")
    print(result)
    return 'Executing message'