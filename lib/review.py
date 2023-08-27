class Review:
    
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.all_reviews.append(self)

    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews
    
    def get_customer(self):
        return self.customer
    
    def get_restaurant(self):
        return self.restaurant
    
    
