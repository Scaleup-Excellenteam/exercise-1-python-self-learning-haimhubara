def cup_of_join(sep=None, **kwargs):
    """
    the func get couple lists and merge them into one list and if we add seperator,
     the func will add the seperator between every list

     params: seperator and lists
     return: merge the lists into one list with seperator between every list
    """
    result_list = []
    count = 0
    length = len(kwargs)
    if sep:
        for key in kwargs:
            result_list += kwargs[key]
            count += 1
            if count < length :
                result_list.append(sep)
    else:
        for key in kwargs:
            result_list += kwargs[key]
            count += 1
            if count < length:
                result_list.append(",")

    return result_list

if __name__ == "__main__":
    result_list = cup_of_join( list1=[12,12,12], list2=[12,12,12])
    print("result_list: ", result_list)
