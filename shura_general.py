import itertools

import pycosat


def get_int_arg(description: str, checker=None, checker_error_desc=''):
    arg = input(description)
    try:
        temp_val = int(arg)
        if checker is not None and not checker(temp_val):
            print(checker_error_desc or "You have entered a wrong thing")
            return get_int_arg(description, checker)
        return temp_val
    except ValueError:
        print("You have entered a wrong thing")
        return get_int_arg(description, checker)


n_number_size = get_int_arg("Please, enter n_number size: ", lambda a: a >= 3, 'N-number length should be 3 or more')
start = get_int_arg("Please, enter start of set: ")
end = get_int_arg("Please, enter end of set: ", lambda a: a - start >= n_number_size + 1,
                  'Set length should be more than n_number length + 1')

set_of_numbers = range(start, end + 1)
print(f'Set = {list(set_of_numbers)}')

combinations = itertools.combinations(set_of_numbers, n_number_size)
cnf = []
for i in combinations:
    arr = i
    if all(k < 0 for k in i):
        arr = sorted(i, reverse=True)
    elif 0 in i:
        temp = list(i)
        temp.remove(0)
        temp.append(0)
        arr = temp
    target_sum = arr[-1]
    remaining_sum = sum(arr[:-1])
    if target_sum == remaining_sum:
        print(arr)
        var_n = []
        var_p = []
        for n in arr:
            new_n = n - start + 1
            var_n.append(-abs(new_n))
            var_p.append(abs(new_n))
        cnf.append(var_n)
        cnf.append(var_p)

print(cnf)
print(pycosat.solve(cnf))
