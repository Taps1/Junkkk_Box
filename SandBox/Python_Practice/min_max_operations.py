def get_max_min():
    file_name = raw_input()
    dd = {}
    with open(file_name) as fh:
        for item in fh.readlines():
            key, value = item.strip('\n').split(',')
            dd.setdefault(key, []).append(value)
        for dict_item in dd:
            print dict_item, min(dd.get(dict_item)), max(dd.get(dict_item))
        
        

if __name__ == "__main__":
    get_max_min()
