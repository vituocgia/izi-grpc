from cachext.exts import Cache
from peeweext.izi_grpc import Peeweext
from izi_grpc.contrib.extensions.celery import Celery

cache = Cache()
pwx = Peeweext()
celeryapp = Celery()
