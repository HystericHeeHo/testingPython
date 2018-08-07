import os 

dir_fd = os.open('somedir', 'r')
def opener(path, flags):
    return os.open(path, flags, dir_fd=dir_fd)