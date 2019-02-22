if __name__ == '__main__':
    months, rabbit_pairs_producing = map(int, input().split())
    children = 1
    grow_ups = 0

    for i in range(months - 1):
        next_children = grow_ups * rabbit_pairs_producing
        grow_ups += children
        children = next_children
    print(grow_ups + children)


# next = grow_up_pairs * rabbit_pairs_producing + prev
#
# 1     0g 1c
# 2     1g 0c
# 3     1g 3c
# 4     4g 3c
# 5     7g 12c
# total = 19
