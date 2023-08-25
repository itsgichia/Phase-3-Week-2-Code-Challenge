class Review:

    all_reviews = []
    # Initialize a Review object with a customer, restaurant and rating
    def __init__(self, customer, restaurant, rating:int):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.all_reviews.append(self)

    def get_rating(self):
        return self.rating
    
    def set_rating(self, new_rating):
        self.rating = new_rating

    @classmethod
    def all(cls):
        return cls.all_reviews