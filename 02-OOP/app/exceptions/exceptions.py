class DuplicateProductError(Exception):
    pass

class DuplicateCategoryError(Exception):
    pass

class DuplicateSupplierError(Exception):
    pass

class ProductNotFoundError(Exception):
    pass

class CategoryNotFoundError(Exception):
    pass

class SupplierNotFoundError(Exception):
    pass

class InsufficientStockError(Exception):
    pass