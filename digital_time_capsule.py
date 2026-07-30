# Digital Time Capsule

print("*" * 65)
print("Welcome to Your Digital Time Capsule")
print("*" * 65)
print("\n")


name = input("Enter your name: ")
current_date = input("Enter today's date and time (dd/mm/yyyy hh:mm): ")
current_age = int(input("What is your age at the time of creating your capsule: "))
current_course = input("What are you studying right now?: ")
dream_career = input("What career, if any, are you working towards?: ")

print("\n")

print("Now let's talk about life outside your academics...")
current_skillmaxx = input("Name one skill you are currently learning: ")
main_2026_goal = input("What is your biggest goal this year?: (My main goal is to...)")

print("\n")

print("Reflecting on the year so far...")
favourite_quote = input("Enter a quote that has stuck with you this year: ")
core_memory = input("What's one thing you want to remember forever from this year?: ")

print("\n")

print("And to your future self...")
future_message = input("Enter a message to your future self: ")

print("\n")

print("Now let's put it all together...")

print("\n")

print("=" * 50)
print(f"{name}'s Digital Time Capsule")
print("=" * 50)

print(f"At the initialisation of my capsule, I am {current_age} years old.")
print(f"I'm studying {current_course} towards a career in {dream_career}.")
print(f"In my spare time, I like to dabble in {current_skillmaxx}.")
print(f"My main goal for 2026 is to {main_2026_goal}.")

print("\n")

print(f"Reflecting on the year so far, a quote that has really stuck with me is {favourite_quote}.")
print(f"I hope I never forget {core_memory}.")

print("\n")

print(f"To my future self, I'd like to say: {future_message}.")

print("\n")

print("With love,")
print(name)
print(current_date)