def largest_prime_factor():
    prime_factors = [1]
    number = input("Please provide a number: ")
    import pdb;pdb.set_trace()
    for i in range(2, number/2+1):
        Flag = True
        while Flag and reduce(lambda x, y: x*y, prime_factors) < number:
            if not number % i == 0:
                Flag = False
            else:
		prime_factors.append(i)
    print "PRIME FACTORS ARE: ", prime_factors

if __name__ == "__main__":
    largest_prime_factor()
