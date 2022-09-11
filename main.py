def join_sort_array(array_lst1: list, array_lst2: list) -> list:
    new_array_lst1 = [str(array_lst1[num]) for num in range(len(array_lst1))]
    new_array_lst2 = [str(array_lst2[num]) for num in range(len(array_lst2))]
    str_new_array_lst1 = '#'.join(new_array_lst1)
    str_new_array_lst2 = '#'.join(new_array_lst2)
    str_result = str_new_array_lst1 + '#' + str_new_array_lst2
    str_result = str_result.split('#')
    new_str_result = [int(str_result[num]) for num in range(len(str_result))]
    return new_str_result


def sort_array_bubble(array_result: list) -> list:
    for item_i in range(1, len(array_result), 1):
        for item_j in range(0, len(array_result)-1, 1):
            if array_result[item_j] > array_result[item_j+1]:
                t = array_result[item_j]
                array_result[item_j] = array_result[item_j+1]
                array_result[item_j + 1] = t
    return array_result


array_lst1 = [1, 2, 3, 4]
array_lst2 = [5, 6, 7, 8]

new_list = join_sort_array(array_lst1, array_lst2)
new_list.reverse()

print(new_list)
print(sort_array_bubble(new_list))