def second_let(one_string: str) -> str:
    return one_string[1]
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

sorted_by_second_let = sorted(ex_lst, key=second_let)

print(sorted_by_second_let)
