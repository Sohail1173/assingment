import random
import string
import concurrent.futures

# define a function to generate a random filename
def generate_filename():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(10)) + '.txt'

# define a function to save a file with a random number
def save_file(filename):
    with open(filename, 'w') as f:
        num = random.randint(1, 1000)
        f.write(str(num))

# create a thread pool with 5 services
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # submit a task to each service
    for i in range(5):
        filename = generate_filename()
        executor.submit(save_file, filename)
        print(f'Submitted task to save {filename}')
