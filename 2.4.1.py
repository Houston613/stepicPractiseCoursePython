
with open('dataset_24465_4.txt') as file:
    lines = file.read().splitlines()


with open('result.txt', 'w') as file2:
    for line in lines[::-1]:
        file2.write('%s\n' % line)

