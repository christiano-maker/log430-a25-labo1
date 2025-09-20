from daos.product_dao import ProductDAO

class ProductController:
    def __init__(self):
        self.dao = ProductDAO()

    def list_products(self):
        return self.dao.select_all()

    def create_product(self, product):
        return self.dao.insert(product)
    
    def update_user(self, product):
        """ Create a new user based on user inputs """
        self.dao.update(product)

    def delete_product(self, product_id):
        return self.dao.delete(product_id)

    def shutdown(self):
        self.dao.close()