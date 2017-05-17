class PrimeNumber(object):
    """This method will calculate If the number is prime or not"""
    def __init__(self, number):
        self.number = number

    def is_prime(self):
        input_number = [num for num in range(2, self.number-1)]
        prime = False
        for num in input_number:
            if self.number % num == 0:
                prime = True
                break
        if prime: 
            print "Number", self.number, " is Prime number"
        else: 
            print "Number", self.number, " is not prime"

if __name__ == "__main__":
    obj = PrimeNumber(7)
    obj.is_prime()
