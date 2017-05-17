class Square_Root(object):
    """This class will calculate Square Root for the given number"""
    def __init__(self, number):
        self.number = number
        self.fractions  = []

    def get_fractions(self):
        # making fractions for the number
        num_arr = [num for num in range(2, self.number/2+1)]
        for num in num_arr:
            if self.number % num == 0:
                while self.number % num == 0:
                    self.number /= num
                    self.fractions.append(num)
        print self.fractions

if __name__ == "__main__":
    obj = Square_Root(3)
    obj.get_fractions()
        
