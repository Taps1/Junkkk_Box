def _main():
    """."""
    maximum_term = input("Please provide a value for maximum term: " )
    item, first, second = 0, 1, 2
    ll = [first]
    while second < maximum_term:
        first, second = second, first + second
        ll.append(first)
    print "list is: ", ll
    print "Sum is: ", sum([i for i in ll if i % 2 == 0])
        

if __name__ == '__main__':
    _main()
