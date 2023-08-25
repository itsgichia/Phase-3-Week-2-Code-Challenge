class Customer:
    all_customers = []
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.all_customers.append(self)

    def get_given_name(self):
        return self.given_name
    
    def set_given_name(self, new_given_name):
        self.given_name = new_given_name

    def get_family_name(self):
        return self.family_name
    
    def set_family_name(self, new_family_name):
        self.family_name = new_family_name
        
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers  
    
