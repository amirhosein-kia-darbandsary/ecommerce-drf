import pytest

pytestmark = pytest.mark.django_db


class TestCategoryEndPoint:
    
    endpoint = "/api/category/"
    
    def test_category_get(self,category_factory,api_client):
        # Arrange
        x = category_factory.create_batch(4)
        # Act 
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        assert len(response.json()) == 4

class TestProductEndPint:
    endpoint = "/products/"
    
    def test_product_get(self, product_factory, api_client):
        # Arrange
        x = product_factory()
        # Act core
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        assert len(response.json()) == 1
        
        
class TestBrandEndPoint:
    endpoint = "/api/brand/"
    
    def test_brand_get(self, brand_factory, api_client):
        # Arrange
        x = brand_factory.create_batch(4)
        # Act  
        response = api_client().get(self.endpoint)
        print(response.content)
        # Assert
        assert response.status_code == 200
        assert len(response.json()) == 4
        
