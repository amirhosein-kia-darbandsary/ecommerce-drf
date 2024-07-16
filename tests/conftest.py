import pytest
import pytest_factoryboy
from rest_framework.test import APIClient

from .factories import BrandFactory, CategoryFactory, ProductFactory, ProductLineFactory

pytest_factoryboy.register(CategoryFactory)
pytest_factoryboy.register(BrandFactory)
pytest_factoryboy.register(ProductFactory)
pytest_factoryboy.register(ProductLineFactory)


@pytest.fixture
def api_client():
    return APIClient