def display_dictionaty_conent(some_dictionary):
    for key, value in some_dictionary.items():
        print(key, ":", str(value))


def display_tuple_content(some_tuple):
    for index, item in enumerate(some_tuple):
        print(index, item)


# Iterate through list and display indexed content
def display_list_content(some_list):
    for index in range(len(some_list)):
        element = some_list[index]
        print(index + 1, element)
