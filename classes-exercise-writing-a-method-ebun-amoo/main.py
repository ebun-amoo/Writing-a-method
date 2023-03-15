import os

class File:
    def __init__(self, path):
        self.path = path
        
    def get_size(self):
        return os.path.getsize(self.path)
    
    def set_contents(self, contents):
        with open(self.path, 'w') as f:
            f.write(contents)
            
    def print_contents(self):
        f = open(self.path,'r',encoding = 'utf-8')
        for line in f:
           print(f"{line}")


test_file = File('test.txt')
test_file.set_contents('hello')
size_of_file = test_file.get_size()
print(f'we just wrote to a file named {test_file.path}')
print(f'the size of the file is {size_of_file} bytes')
test_file.print_contents()
