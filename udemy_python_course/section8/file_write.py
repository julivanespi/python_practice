'''
This example will show how to write to a file
'''



def main():
    '''
    In the main, the first thing we have to do is open the file.
    We named the variable that represents the file 'out' and we passed
    the a flag of 'a'
    The 'a' is for append
    '''
    out = open("test.txt", "a")
    for i in range(5):
        input_to_file = input("Enter string to write to file: ")
        out.write("\n{}".format(input_to_file))
    out.close()

if __name__ == "__main__":
    main()