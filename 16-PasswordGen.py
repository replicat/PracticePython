import random
import string

# The classic one-liner
print("".join(random.choice(string.ascii_letters+string.digits+string.punctuation) for i in range(random.randint(8, 16))))