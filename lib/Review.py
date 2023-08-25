class Review:
    # Empty review list
    all_reviews = []

    # Initialize a Review object with a customer, restaurant and rating
    def __init__(self, customer, restaurant, rating:int):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.all_reviews.append(self)

    # Getter method to retrieve the review
    def get_rating(self):
        return self.rating
    
    # Setter method to set a new rating
    def set_rating(self, new_rating):
        self.rating = new_rating

    # Retrieve all the reviews
    @classmethod
    def all(cls):
        return cls.all_reviews