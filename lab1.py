
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError()
    if len(int_list) == 0:
        return None

    high = -9223372036854775807
    for x in int_list:
        if x > high:
            high = x
    return high


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError()

    if len(int_list) <= 1:
        return int_list
    last = int_list.pop(0)
    reverse_rec(int_list).append(last)
    return int_list

def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    pass
"""
def main():
    print(reverse_rec([1,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8]))

if __name__ == "__main__":
    main()
"""