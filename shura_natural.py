import itertools

import pycosat


def get_int_arg(description: str, checker=None, checker_error_desc=''):
    arg = input(description)
    try:
        temp = int(arg)
        if checker is not None and not checker(temp):
            print(checker_error_desc or "You have entered a wrong thing")
            return get_int_arg(description, checker)
        return temp
    except ValueError:
        print("You have entered a wrong thing")
        return get_int_arg(description, checker)


n_number_size = get_int_arg("Please, enter n_number size: ", lambda a: a >= 3, 'N-number length should be 3 or more')
start = get_int_arg("Please, enter start of set: ", lambda a: a >= 1, "First set element should be 1 or more")
end = get_int_arg("Please, enter end of set: ", lambda a: a - start >= n_number_size + 1,
                  'Set length should be more than n_number length + 1')

set_of_numbers = range(start, end + 1)
print(f'Set = {list(set_of_numbers)}')

combinations = []
cnf = []
for i in itertools.combinations(set_of_numbers, n_number_size):
    target_sum = i[-1]
    remaining_sum = sum(i[:-1])
    if target_sum == remaining_sum:
        combinations.append(i)
        var_n = []
        var_p = []
        for n in i:
            new_n = n - start + 1
            var_n.append(-new_n)
            var_p.append(new_n)
        cnf.append(var_n)
        cnf.append(var_p)

print(combinations)
print(cnf)
print(pycosat.solve(cnf))
for i in itertools.islice(pycosat.itersolve(cnf), 5):
    print([int((abs(j) + start - 1) * j / abs(j)) for j in i])
