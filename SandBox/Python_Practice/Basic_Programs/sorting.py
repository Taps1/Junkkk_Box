class Sorting_Methods(object):
    """This class provides multiple sorting methods"""
    def __init__(self):
        # initiation method
        pass

    def sort_an_array(self):
        """This function will receive an array and do the sort on it"""
        array_to_sort = input("Please provide an Unsorted array")
        import pdb;pdb.set_trace()
        sorted_array = []
        for i in range(len(array_to_sort)):
            for item in range(i+1, len(array_to_sort)):
                if array_to_sort[i] > array_to_sort[item]:
                    array_to_sort[item], array_to_sort[i] = array_to_sort[i], array_to_sort[item]
        print array_to_sort

if __name__ == "__main__":
    obj = Sorting_Methods()
    obj.sort_an_array()
        
