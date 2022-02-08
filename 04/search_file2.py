import os

queue = ['/']

while len(queue) > 0:
    dir = queue.pop()
    for i in os.listdir(dir):
        if i == 'book':
            print(dir + i)
        if os.path.isdir(dir + i):
            if os.access(dir + i, os.R_OK):
                queue.append(dir + i + '/')
