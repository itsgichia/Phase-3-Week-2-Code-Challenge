from customer import Customer
from restaurant import Restaurant
from review import Review

customer1 = Customer("JB", "Tomashi")
customer2 = Customer("Carlton", "Wambua")
customer3 = Customer("Netan", "Kapaya")
customer4 = Customer("Yasmine", "Julia")

rest1 = Restaurant("KFC")
rest2 = Restaurant("Chicken Inn")
rest3 = Restaurant("Kenchic")

review1 = Review(customer1, rest2, 8)
review2 = Review(customer3, rest2, 7)
review3 = Review(customer1, rest1, 10)

# print(review1.customer)
# print(review2.restaurant)
# print(review3.rating)

# print(rest2.reviews)

# Restaurant reviews
# rest2.display_reviews()

# Restaurant customers
# print(rest2.customers())

# Customer restaurants
# print(customer1.restaurants())

# Customer add_review
# added_review = customer4.add_review(rest2, 9)
# print(f"{added_review.restaurant.name}, {added_review.rating}")





