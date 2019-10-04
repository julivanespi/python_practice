import datetime

def main():
    # main code function
    print("Hello there")
    DOB=input("Enter the year you were born: ")
    CurrentYear=datetime.datetime.now().year
    Age=CurrentYear-int(DOB)
    print("Your age is {}".format(Age))



# this line is important so that the python file can 'start' at 'main()'
# you don't have to put the :main()
# in this example, this file will start with the running the main() method
if __name__ == '__main__':main()