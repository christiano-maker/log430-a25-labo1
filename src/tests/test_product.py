from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
    product_list = dao.select_all()
    assert len(product_list) >= 3

def test_product_insert():
    product = Product(None, 'MX Master 3', 'Logitech', 129.90)
    dao.insert(product)
    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name in names

def test_product_update():
    product = Product(None, 'Keyboard', 'KeyCo', 99.00)
    assigned_id = dao.insert(product)

    corrected_price = 129.00
    product.id = assigned_id
    product.price = corrected_price

    dao.update(product)

    product_list = dao.select_all()
    prices = [p.price for p in product_list]
    assert corrected_price in prices

def test_product_delete():
    product = Product(None, 'ToDelete', 'BrandX', 9.99)
    assigned_id = dao.insert(product)
    dao.delete(assigned_id)

    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name not in names