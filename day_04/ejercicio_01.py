import random

# My option
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_number = random.randint(0, len(friends) - 1)

print(friends[random_number])

# 1 Option
print(random.choice(friends))

# 2 Option
random_index = random.randint(0,4)
print(friends[random_index])


