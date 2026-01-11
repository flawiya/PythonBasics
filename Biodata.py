Name = "Flawiya S. More"
Age = 24
City = "Liverpool, UK"
Degree = "MSc Geographical Data Science"
Foods = ["Biryani", "Samosa", "Idli"]

print("=== MY INFO ===")
print(f"Name: {Name}")
print(f"Age: {Age}")
print(f"City: {City}")
print(f"Currently studying: {Degree}")
print("Favorite foods:", ", ".join(Foods))

# Interactive part
user_food = input("\nWhat's your favorite food? ")
print(f"Great choice, {user_food}!")
