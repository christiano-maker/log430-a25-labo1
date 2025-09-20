"""
Product view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from models.product import Product
from controllers.product_controller import ProductController

class ProductView:
    @staticmethod
    def show_options():
        """ Show menu with operation options which can be selected by the user """
        controller = ProductController()
        while True:
            print("\n1. Montrer la liste d'items\n2. Ajouter un item\n3. modifier un item\n4. supprimer un item\n5. Quitter l'appli")
            choice = input("Choisissez une option: ")

            if choice == '1':
                products = controller.list_products()
                ProductView.show_products(products)
            elif choice == '2':
                name, brand, price = ProductView.get_inputs()
                product = Product(None, name, brand, price)
                controller.create_product(product)
            elif choice == '3':
                product_id_str = input("ID de l'item à modifier: ").strip()
                productid = int(product_id_str)
                name, brand, price = ProductView.get_inputs()
                product = Product(productid, name, brand, price)
                controller.update_product(product)
            elif choice == '4':
                product_id_str = input("ID de l'item à supprimer: ").strip()
                productid = int(product_id_str)
                controller.delete_product(productid)
            elif choice == '5':
                controller.shutdown()
                break
            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def show_products(products):
        """ List products """
        print("\n".join(f"{p.id}: {p.name} ({p.brand}) - {p.price}" for p in products))

    @staticmethod
    def get_inputs():
        """ Prompt user for inputs necessary to add a new product """
        name = input("Nom de l'item : ").strip()
        brand = input("Marque : ").strip()
        price = float(input("Prix : ").strip())
        return name, brand, price
