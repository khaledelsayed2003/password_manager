import random
import string

def generate_password():
    """Generate a strong random password with letters, digits, and symbols."""
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!#$%&*()+"
    
    # List Comprehension used...
    password_list = (
        [random.choice(letters) for _ in range(6)] +
        [random.choice(numbers) for _ in range(3)] +
        [random.choice(symbols) for _ in range(2)]
    )
    random.shuffle(password_list)
    password = "".join(password_list)
    return password


