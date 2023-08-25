class Review:
    # Empty review list
    all_reviews = []

    # Initialize a Review object with a customer, restaurant and rating
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.all_reviews.append(self)

    def rating(self):
        return self.rating

    # Retrieve all the reviews
    @classmethod
    def all(cls):
        return cls.all_reviews
    
    # - `Review customer()`
    # - returns the customer object for that review
    # - Once a review is created, should not be able to change the customer
    def customer(self):
        return self.customer
    
    def restaurant(self):
        return self.restaurant
    
    
