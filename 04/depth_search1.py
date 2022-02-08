tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
        [13, 14], [], [], [], [], [], [], [], []]

def search(pos):
    print(pos, end=' ')
    for i in tree[pos]:
        search(i)
search(0)
