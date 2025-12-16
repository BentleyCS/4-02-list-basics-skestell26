def bookends(li: list)-> list:
    first = li.pop(0)
    last = li.pop()
    return [first, last]
    """
    Given a list of numbers remove the first and last elements from the list and
    return a new list of those two elements.
    You can assume any list given is at least 2 elements long.
    Example list of [1,5,7,3,2] the original list would become [5,7,3] and the new
    list would be [1,2]
    :param list:
    :return:
    """

def inOrder(li: list) -> bool:
    return li == sorted(li)
    """
    Given a list of numbers return true if the list is in ascending order.
    :param list:
    :return:
    """


def find(li: list, target: int)-> int:
    for i in range (len(li)):
        if li[i] == target:
            return i
    return -1

    """
    Given a list of numbers and a target value return the index location of the
    target value within the list.
    If the target value is not in the list return -1
    If multiple of the target value exist within the list you may return either
    index.
    You are not alowed to use the built-in index method from python.
    Example list [1,3,5,7,9] target = 3 returned value would be 1 because 3 can be
    found at the first index.
    Example list [3, 7, 8, 1, 0, 1, 12] target = 1 a return of either 3 or 5 would
    be valid.
    Example list [1,3,5,6,9] target 7 returns -1 because 7 is not within the list.
    :param list:
    :param target:
    :return:
    """


def removeLowest(li: list) -> None:
    lowest_index = 0

    for i in range (1, len(li)):
        if li[i] < li[lowest_index]:
            lowest_index = i

    li.pop(lowest_index)
    """
    Given a list of numbers remove the lowest element from the list. You may assume the list is at least 1 element long.
    If there are multiple of the lowest number you just need to remove 1.
    Example list [3,6,7,2,12] would become [3,6,7,12]
    :param list:
    :return:
    """


def keepOrder(li: list, value) -> None:
    for i in range(len(li)):
        if value <= li[i]:
            li.insert(i, value)
            return
    li.append(value)
    """
    Given a list of numbers that is in order and a value. Place the value into the
    list such that the list is still in order.
    Example list=[1,3,5,6] value =4 the resulting list would be [1,3,4,5,6]
    :param list:
    :param value:
    :return:
    """


def merge(l1: list, l2: list) -> list:
    merged = []
    i = j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    # Add any remaining elements
    while i < len(l1):
        merged.append(l1[i])
        i += 1

    while j < len(l2):
        merged.append(l2[j])
        j += 1

    return merged
    """
    Given two lists that are in order. produce a new list that is the two lists merged together and in order.
    Make sure to now modify either of the original lists.
    Example l1 = [1,3,5] l2 = [2,4,6,8] -> [1,2,3,4,5,6,8]
    :param l1:
    :param l2:
    :return:
    """
