import pytest
import logging
import os
from io import StringIO

import izi_grpc
from izi_grpc.test.fixtures import *  # noqa


@pytest.fixture
def logstream():
    return StringIO()


@pytest.fixture
def app(logstream):
    os.environ.setdefault('IZI_ENV', 'testing')
    logger = logging.getLogger('izi_grpc')
    h = logging.StreamHandler(logstream)
    logger.addHandler(h)
    root = os.path.join(os.path.dirname(__file__), 'wd')
    app = izi_grpc.create_app(root)
    yield app
    logger.removeHandler(h)
    izi_grpc._app = None
