class Max_Min(object):
    def __init__(self):
        pass

    def get_max(self, seq):
        self.seq = seq
        max_value = self.seq[0]
        for i in range(1, len(self.seq)):
            if self.seq[i] > max_value:
                max_value = self.seq[i]
        print "Maximum Value is: ", max_value

    def get_min(self, seq):
        self.seq = seq
        min_value = self.seq[0]
        for i in range(len(self.seq)):
            if self.seq[i] < min_value:
                min_value = self.seq[i]
        print "Minimum Value is", min_value

if __name__ == "__main__":
    arr_to_operate = [4,12,90,54,87,1,43]
    obj = Max_Min()
    obj.get_max(arr_to_operate)
    obj.get_min(arr_to_operate)

