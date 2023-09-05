import random
import time

names = ['Sunny', 'Bunny', 'Chinny', 'Vinny']
subjects = ['Python', 'Java', 'Blockchain']

# Function to create a list of people
def people_list(num_people):
    results = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'subject': random.choice(subjects)
        }
        results.append(person)
    return results

# Generator function to yield people one by one
def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(subjects)
        }
        yield person

# Measure the time taken to create a large collection of people using a list
t1 = time.perf_counter()
people = people_list(1000000)  # Uncomment this line to use the list-based approach
t2 = time.perf_counter()
print('Took {:.6f} seconds'.format(t2 - t1))
# Measure the time taken to create the same collection of people using a generator
t1 = time.perf_counter()
people = people_generator(1000000)
t2 = time.perf_counter()

print('Took {:.6f} seconds'.format(t2 - t1))

# Generators vs. Normal Collections wrt Memory Utilization:
# Normal Collection:
# l = [x * x for x in range(10000000000000000)]
# We will get a MemoryError in this case because all these values are required to store in the memory.

# Generators:
# g = (x * x for x in range(10000000000000000))
# We won't get any MemoryError because the values won't be stored at the beginning.
