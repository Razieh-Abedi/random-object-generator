import random
import string
import time

# Function to generate a random alphabetical string
def random_alpha_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Function to generate a random real number
def random_real_number():
    return round(random.uniform(-1000.0, 1000.0), 2)

# Function to generate a random integer
def random_integer():
    return random.randint(-1000, 1000)

# Function to generate a random alphanumeric string with spaces before and after
def random_alphanumeric():
    alphanumeric = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # Add random spaces before and after the string (total spaces < 10)
    return f"{' ' * random.randint(0, 5)}{alphanumeric}{' ' * random.randint(0, 5)}"

# Function to generate a random object
def random_object():
    return random.choice([random_alpha_string, random_real_number, random_integer, random_alphanumeric])()

# Function to write to a file until it reaches 10MB
def generate_file(filename, target_size=10 * 1024 * 1024):
    with open(filename, 'w') as file:
        start_time = time.time()
        while file.tell() < target_size:
            obj = random_object()
            file.write(f"{obj},")
        print(f"File generated in {time.time() - start_time:.2f} seconds.")

# Run the generation for a 10MB file
generate_file("random_objects.txt")
