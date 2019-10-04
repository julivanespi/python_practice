'''
This example will show how to read a file. The thing to remember is to close the file at the end.
'''



def main():
    '''
    This example will show how to read a file
    '''
    read_file = open("test.txt", "r")
    for line in read_file:
        print(line)
    read_file.close()

if __name__ == "__main__":
    main()