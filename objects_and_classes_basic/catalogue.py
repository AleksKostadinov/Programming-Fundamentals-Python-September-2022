class Catalogue:

    def __init__(self, name: str):
        self.products = []
        self.name = name

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [product for product in self.products if product[0] == first_letter]

    def __repr__(self):
        result = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{result}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
