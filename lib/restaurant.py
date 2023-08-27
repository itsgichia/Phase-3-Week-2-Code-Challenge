from review import Review
class Restaurant:
    
    def __init__(self, name:str):
        self._name = ""
        self.name = name 

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print("Restaurant name should be a string!")
            
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
            
    def average_star_rating(self):
        total_ratings = 0
        total_reviews = 0

        for review in self.reviews():
            total_ratings += review.rating
            total_reviews += 1

        if total_reviews == 0:
            return 0
        
        return total_ratings / total_reviews