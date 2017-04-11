def yield_multiple(maximum_number, multiple_one, multiple_two):
    for number in range(1, maximum_number):
        if number % multiple_one == 0 or number % multiple_two == 0:
            yield number

def calculate_sum_of_prime_number():
    """."""
    maximum_number = input("Please provide the number: ")
    multiples = input("Please provide two multiples: ")
    multiple_one, multiple_two = multiples
    dd = yield_multiple(maximum_number, multiple_one, multiple_two)
    print "Sum is: ", sum(dd)

if __name__ == "__main__":
    calculate_sum_of_prime_number()
