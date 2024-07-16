import pytest 

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_str_method(self, category_factory):
        x = category_factory()
        assert x.__str__() == "test_str_method_cat"
        
        
    
    

class TestBrandModel:
    def test_str_method(self, brand_factory):
        x = brand_factory()
        assert x.__str__() == "test_str_method_bra"
        
    

class TestProductModel:
    def test_str_method(self, product_factory):
        x = product_factory()
        assert x.__str__() == 'Product 1'
    
    def test_save_generates_slug(self, product_factory):
        # Arrange
        product = product_factory(name="Test Product", slug=None)
        
        # Act
        product.save()
        
        # Assert
        assert product.slug == "test-product"

    def test_save_maintains_existing_slug(self, product_factory):
        # Arrange
        product = product_factory(name="Another Product", slug="existing-slug")
        
        # Act
        product.save()
        
        # Assert
        assert product.slug == "existing-slug"

    def test_unique_slug_constraint(self, product_factory):
        # Arrange
        product_factory(name="Unique Product", slug="unique-slug")
        
        with pytest.raises(Exception):
            # Act
            product_factory(name="Another Unique Product", slug="unique-slug")

    def test_blank_slug_field(self, product_factory):
        # Arrange
        product = product_factory(name="Blank Slug Product", slug="")
        
        # Act
        product.save()
        
        # Assert
        assert product.slug == "blank-slug-product"

    def test_null_slug_field(self, product_factory):
        # Arrange
        product = product_factory(name="Null Slug Product", slug=None)
        
        # Act
        product.save()
        
        # Assert
        assert product.slug == "null-slug-product"
        
class TestProductLineModel:
    def test_str_method(self, product_line_factory):
        x = product_line_factory(sku="1234")
        assert x.__str__() == '1234'