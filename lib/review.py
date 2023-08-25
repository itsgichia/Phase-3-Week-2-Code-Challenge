class Review:
    # Empty review list
    all_reviews = []

    # Initialize a Review object with a customer, restaurant and rating
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.all_reviews.append(self)

    # Returns the rating for a restaurant
    def rating(self):
        return self.rating

    # Retrieve all the reviews
    @classmethod
    def all(cls):
        return cls.all_reviews
    
    # Returns customer object for that review
    def get_customer(self):
        return self.customer
    
    # Returns restaurant object for that review
    def get_restaurant(self):
        return self.restaurant
    
    
