# 1. Write a python code to remove an element from a tuple.

def remove_tuple_element():
    old_tuple = (1, 4, 7, 9, 10, 13, 64)
    new_list = []
    remove = 10

    print(f'The next lines of code will remove the element "{remove}" from tuple {old_tuple}\n'
          f'and will cast the list into a tuple.')
    print("____________________________________________________________________________")

    for element in old_tuple:
        if element != remove:
            new_list.append(element)

    print(f'This is a list from which the "{remove}" element has been removed: {new_list}')

    new_tuple = tuple(new_list)

    print(f'This is the new tuple, obtained by casting the list: {new_tuple}')

    print("____________________________________________________________________________")

    # 2. Replace the last element in the list with the string 'last' using list comprehension and tuples


def replace_last():
    first_list = [1, 4, 6, 'a', 'string', 'abc', 'element', 'music', 45, 62, 6.8, 5.0]
    second_list = [56, 89, 'test', 'abc', 'random', 6.7, (4, 6), [1, 4, 6]]
    third_list = []

    first_list[-1] = 'last'
    print(first_list)

    for elem in second_list:
        if second_list.index(elem) == len(second_list) - 1:
            elem = 'last'
            third_list.append(elem)
        else:
            third_list.append(elem)

    print(third_list)

    print("____________________________________________________________________________")


# 3. Extract only the strings from the following list using list comprehension :
# slist = ['I', 'am', 1, 'list', 'of', 5, 'strings']


def extract_strings():
    slist = ['I', 'am', 1, 'list', 'of', 5, 'strings']

    string_list = [x for x in slist if isinstance(x, str)]

    print(string_list)


# 4. Generate a 3 by 3 matrix that contains 'X' on the main diagonal and '_' in the rest.
#       X _ _
#       _ X _
#       _ _ X


if __name__ == '__main__':
    remove_tuple_element()
    replace_last()
    extract_strings()
