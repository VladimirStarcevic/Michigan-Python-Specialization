from typing import List, Any

def snames(list_in: List[str]) -> List[str]:
    copy_list = list_in[:]

    list_to_return = []

    for item in copy_list:
        if item.lower().startswith('s'):
            list_to_return.append(item)
    return  list_to_return

def sname(name: str) -> Any:
    if name.lower().startswith('s'):
        return name
    return None

def snames_with_filter_and_sname(list_in: List[str]) -> List[str]:
     return list(filter(sname, list_in))

def snames_with_filter_and_lambda(list_in: List[str]) -> List[str]:
    return list(filter(lambda name: name.lower().startswith('s'), list_in))


names = ["Jack", "Samantha", "Nelson", "Swathi", "Shu-fen"]
lastnames = ["Vikander", "Anderson", "Tyler", "Anand" ,"Li"]

s_list = snames(names)
print(s_list)
assert snames(names) == ['Samantha', 'Swathi', 'Shu-fen']

print("\n=========== Snames with Filter and sname=============")

s_list2 = snames_with_filter_and_sname(names)
print(s_list2)

assert snames_with_filter_and_sname(names) == ['Samantha', 'Swathi', 'Shu-fen']

print("\n=========== Snames with Lambda =============")

s_list3 = snames_with_filter_and_lambda(names)
print(s_list3)

assert snames_with_filter_and_lambda(names) == ['Samantha', 'Swathi', 'Shu-fen']




