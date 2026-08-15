class Supplier:
    next_id = 1

    def __init__(self, company_name, email = None, phone = None):
        self.s_id = Supplier.next_id
        Supplier.next_id += 1

        self.company_name = company_name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"""    
    Name:{self.company_name}
    Email:{self.email}
    Phone:{self.phone}
    """