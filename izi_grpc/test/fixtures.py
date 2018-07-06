import pytest

from izi_grpc import current_app


@pytest.fixture
def app():
    return current_app


@pytest.fixture
def cache(app):
    cache = app.extensions.cache
    cache.clear()
    yield cache
    cache.clear()
