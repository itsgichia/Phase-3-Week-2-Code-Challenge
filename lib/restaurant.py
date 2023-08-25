from review import Review
from customer import Customer
class Restaurant:
    # Initialize a Restaurant object with an empty name
    def __init__(self, name:str):
        self._name = ""
        self.name = name 

    # Getter method to retrieve the restaurant's name
    def get_name(self):
        return self._name
    
    # Setter method to set the restaurant's name with input validation
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print("Restaurant name should be a string!")

    # Name property created using get_name and set_name
    name = property(get_name, set_name)

    def reviews(self):
        restaurant_reviews = []
        for review in Review.all_reviews:
            if review.restaurant == self:
                restaurant_reviews.append(review)
        return restaurant_reviews
    
    def customers(self):
        customer_names = set()
        for review in self.reviews():
            customer = review.get_customer()
            customer_names.add(customer.full_name())
        return tuple(customer_names)
    
    def display_reviews(self):
        restaurant_reviews = self.reviews
        for review in restaurant_reviews():
            print(f"Rating: {review.rating}")
            
    # def display_customers(self):
    #     restaurant_reviews = self.reviews
    #     for review in restaurant_reviews():
    #         print(f"{review.customer().full_name()}")