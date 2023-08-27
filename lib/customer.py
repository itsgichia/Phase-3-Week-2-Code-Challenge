from review import Review

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
    
    def restaurants(self):
        customer_restaurants = set()
        for review in Review.all_reviews:
            if review.get_customer() == self:
                customer_restaurants.add(review.get_restaurant().get_name())
        return customer_restaurants
    
    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        return new_review

    def num_reviews(self):
        count = 0
        for review in Review.all_reviews:
            if review.get_customer() == self:
                count += 1
        return count
    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None
    
    def display_found_customer(self, name):
        found_customer = Customer.find_by_name(name)
        if found_customer:
            print(f"Found customer: {found_customer.full_name()}")
        else:
            print("Customer not found.")

    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer.given_name == name:
                matching_customers.append(customer)
        return matching_customers
    
    @classmethod
    def display_matching_customers(cls, name):
        matching_customers = cls.find_all_by_given_name(name)
        for customer in matching_customers:
            print(f'Matching customer is: {customer.full_name()}')
    
