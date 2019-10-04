

def another_example():
    try:
        x=int(input("Enter a number and I will return double that value... "))
        print(x*2)
    except ValueError:
        print("Value entered has to be an integer" )

def main():
    try:
        ReadFile=open("sample.txt", "r")
        for line in ReadFile:
            print(line)
        ReadFile.close()
    except IOError:
        print("File not found")


if __name__ == "__main__":
    main()
    another_example()
    print("App is done")
    