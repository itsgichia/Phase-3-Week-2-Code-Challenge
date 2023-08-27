from customer import Customer
from restaurant import Restaurant
from review import Review

customer1 = Customer("Sam", "Tomashi")
customer2 = Customer("Anne", "Marie")
customer3 = Customer("Mary", "Jane")
customer4 = Customer("Yasmine", "Julia")
customer5 = Customer("Sam", "Jobs")

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

# Customer num_reviews
# print(customer1.num_reviews())

# Customer find_by_name
# customer2.display_found_customer("Anne Marie")

# Customer find_all_by_given_name
# Customer.display_matching_customers("Sam")

# Restaurant average_star_rating
# print(rest2.average_star_rating())




