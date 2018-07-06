from .peewee import *
from .celery import *

CACHE_BACKEND = 'Redis'

MIDDLEWARES = [
    'izi_grpc.middleware.ServiceLogMiddleware',
    'izi_grpc.middleware.RpcErrorMiddleware'
]

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

TIMEZONE = 'Asia/Shanghai'
GRPC_GRACE =0
PROMETHEUS_SCRAPE = True
