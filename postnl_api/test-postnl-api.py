from postnl_api import PostNL_API

# Login using your jouw.postnl.nl credentials
postnl = PostNL_API('p.schoumacher@gmail.com', 'Pp7EQYhd!')

# Retrieve relevant incoming packages
print("Getting relevant deliveries")
rel_deliveries = postnl.get_relevant_deliveries()
for delivery in rel_deliveries:
    print(delivery)

# Retrieve all incoming packages
print("Getting all deliveries")
all_deliveries = postnl.get_deliveries()
for delivery in all_deliveries:
    print(delivery)

# Retrieve sent packages
print("Getting all distributions (sent packages)")
distributions = postnl.get_distributions()
for distribution in distributions:
    print(distribution)

# Retrieve incoming letters
print("Getting all letters, if that function is turned on")
letters = postnl.get_letters()
for letter in letters:
    print(letter)
