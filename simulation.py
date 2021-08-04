import sys
import random
import string
from script import insert_data


def simulation():
    """
    Function generates a random date and uploads it to the database after printing it.
    """
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(int(input())))
    insert_data(result_str)
    sys.stdout.write(result_str)
    sys.stdout.write('\n')
