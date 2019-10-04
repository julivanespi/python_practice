# this file shows simple method creation
# for these methods to be called, they either have to be invoked in the main, or in another function

def method_with_params(passed_param):
    print("The parameter that was passed was: {}".format(passed_param))

def say_goodbye():
    print("Goodbye world")

def main():
    print("hello world")

if __name__ == "__main__":
    main()
    method_with_params(5)
    say_goodbye()