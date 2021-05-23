def chop(list):
    del list[0]   # removes the first element
    del list[-1]   # removes the last element
    return None


def middle(list):
    new = list[1:]   # stores numbers after the first element
    del new[-1]   # deletes the last element
    return new


my_list = [1, 2, 3, 4]
my_list2 = [1, 2, 3, 4]

chop_list = chop(my_list)
print(my_list)
print(chop_list)  # returns none

middle_list = middle(my_list2)
print(my_list2)
print(middle_list)
