from operator import index

tuple1: tuple[int] = (99,)
tuple2: tuple[int, int, int] = (77, 88, 99,)
tuple3: tuple[int, int, int, int, int, int, int, int, int] = (2, 3, 2, 6, 8, 3, 6, 9, 34)
print(f"first tuple:{tuple1}")
print(f"second tuple:{tuple2}")


def tuple_length(tuple: tuple[any]):
    length = len(tuple)
    return length


print(f"first tuple length:{tuple_length(tuple1)}")
print(f"second tuple length:{tuple_length(tuple2)}")


def tuple_sum(tuple_a: [any], tuple_b: tuple[any]):
    summ = tuple_a + tuple_b
    return summ


print(f"two tuples combined:{tuple_sum(tuple1, tuple2)}")


def same_tuple(tuple_a: tuple[any], tuple_b: tuple[any]):
    set1 = set(tuple_a)
    set2 = set(tuple_b)
    common_elements = set1.intersection(set2)
    return common_elements


print(f"tuple with only common elements:{tuple(same_tuple(tuple1, tuple2))}")


def different_tuple(tuple_a: tuple[any], tuple_b: tuple[any]):
    set1 = set(tuple_a)
    set2 = set(tuple_b)
    diff1 = set1 - set2
    diff2 = set2 - set1
    differences = diff1.union(diff2)
    return differences


print(f"tuple with only different elements:{tuple(different_tuple(tuple1, tuple2))}")


def tuple_index(tup: tuple[any], i):
    try:
        return tup[i]
    except IndexError:
        return None


print(f"the number in index 0 of tuple 1 is :{tuple_index(tuple1, index(0))}")
print(f"the number in index 7 of tuple 2 is :{tuple_index(tuple2, index(7))}")


def reversed_tuple(tup: tuple[any]):
    reversed = tup[::-1]
    return reversed


print(f"the tuple reversed {reversed_tuple(tuple2)}")


def multiply_tuple(tup: tuple[any], number: int):
    mul = tup * number
    return mul


print(f"the tuple multiplied is: {multiply_tuple(tuple1, 4)}")


def tuple_minus_number(tup: tuple[any], number: int):
    removal = [num for num in tup if num != number]
    return removal


print(f"the tuple after number removed:{tuple(tuple_minus_number(tuple2, 88))}")
print(f"the tuple after number removed:{tuple(tuple_minus_number(tuple1, 99))}")


def tuple_no_duplicates(tup: tuple[any]):
    tuple_list: list[int] = []
    [tuple_list.append(number) for number in tup if number not in tuple_list]
    return tuple_list


print(f"the tuple after duplicates been removed:{tuple(tuple_no_duplicates(tuple3))}")


def tuple_index_number(tup: tuple[any], number: int):
    result = [i for i, value in enumerate(tup) if value == number]
    return result


print(f"the indexes for this number are:{tuple(tuple_index_number(tuple3, 3))}")

name_list: list[str] = []
score_list: list[int] = []
counter: int = 0
while True:
    if counter >= 1:
        break
    else:
        names: str = str(input("enter your name:"))
    if names == "done":
        while True:
            scores: int = int(input("enter your score:"))
            if scores == -999:
                break
            else:
                score_list.append(scores)
                counter += 1
    else:
        name_list.append(names)

tuple_names = tuple(name_list)
tuple_scores = tuple(score_list)
combined_tuple = tuple(zip(tuple_names, tuple_scores))
print(combined_tuple)
