class Review:
    # Initialize a Review object with a customer, restaurant and rating
    def __init__(self, customer, restaurant, rating:int):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def get_rating(self):
        return self.rating
    
    def set_rating(self, new_rating):
        self.rating = new_rating

    def all():
        pass  