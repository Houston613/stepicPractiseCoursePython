import os

with open('result.txt', 'w') as file:
    for currentDir, dirs, files in os.walk('main'):
        if list(filter(lambda x: x.endswith('py'), files)):
            file.write('{}\n'.format(currentDir))
