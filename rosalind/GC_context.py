import sys

if __name__ == '__main__':
    counts = {}
    curr_str_name = ''
    total_length = 0
    for line in sys.stdin:
        line = line.strip()
        if line[0] == '>':
            if curr_str_name != '':
                counts[curr_str_name] = counts[curr_str_name] / total_length * 100
            curr_str_name = line[1:]
            counts[curr_str_name] = 0
            total_length = 0
        else:
            counts[curr_str_name] += (line.count('G') + line.count('C'))
            total_length += len(line)
    counts[curr_str_name] = counts[curr_str_name] / total_length * 100

    k_max, v_max = '', 0
    for k, v in counts.items():
        if v > v_max:
            v_max = v
            k_max = k
    print(k_max)
    print(v_max)
