import random, string, timeit
"""
Function that times the generation of a selected string through multiple attempts of random letter selection from exercise on:

https://runestone.academy/runestone/static/pythonds/Introduction/DefiningFunctions.html 

test quote - “methinks it is like a weasel”
"""

def generate_string(length):
    letters = string.ascii_lowercase + ' '
    generated_string = ''.join(random.choice(letters) for i in range(length))
    return generated_string


def generate_shakespeare(quote):
    quote_length = len(quote)
    generated_string = ''
    ctr = 0

    while quote != generated_string:
        ctr += 1
        generated_string = generate_string(quote_length)
        if ctr % 1000000 == 0:
            print("At iteration {}, still running!".format(ctr))

    print("String: {}, generated after {} attempts".format(generated_string, ctr))
    return generated_string, ctr


def time_quotegenerator():
    """time the running of the generator"""

    SETUP_CODE = '''from __main__ import generate_shakespeare'''

    TEST_CODE = '''generate_shakespeare("methinks ")'''

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=1,
                          number=1)

    # printing minimum exec. time
    print(str(times) + ' - Time to generate Shakespeare quote from random strings')

if __name__ == "__main__":
    import datetime
    print("Generator started at {}".format(datetime.datetime.now()))
    time_quotegenerator()
