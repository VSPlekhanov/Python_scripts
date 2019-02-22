def f(task, ans):
    import re

    all_elements = {el for el in task.readline().split()}
    curr_set = set()
    data = task.readlines()
    reactions = dict()

    for line in data:
        separated = line.split('->')
        key = frozenset({el for el in separated[0].split('+')})
        value = {el for el in re.split('\D+', separated[1]) if el != ''}
        if key in reactions:
            reactions[key] = reactions[key].union(value)
        else:
            reactions[key] = value
    while (True):
        for key, value in reactions.items():
            if key.issubset(all_elements):
                curr_set = curr_set.union(value)
        if curr_set.issubset(all_elements):
            break
        all_elements = all_elements.union(curr_set)
        curr_set = set()

    print(all_elements == {el for el in ans.readline().split()})


if __name__ == '__main__':
    for a in range(1, 17):
        # task_path = ""
        with open("/home/viacheslav/Downloads/stepik/test1Hard/" + str(a)) as task:
            with open("/home/viacheslav/Downloads/stepik/test1Hard/" + str(a) + ".clue") as ans:
                print(a)
                f(task, ans)
