
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
    if int_list == None:
        raise ValueError()

    mid = (low+high)//2
    if int_list[mid] == target:
        return mid
    if target < int_list[mid]:
        return bin_search(target, low, mid, int_list)
    if target <= int_list[high]:
        return bin_search(target, mid, high, int_list)
    return None

"""
def main():
    print(bin_search(345, 0, 12, [1,3,8,14,23,45,56,123,234,345,456,567,568]))

if __name__ == "__main__":
    main()
"""