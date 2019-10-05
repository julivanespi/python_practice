class User:
    def __init__(self, userName, age):
        self._UserName = userName
        self._Age = age

    def GetUserName(self):
        return self._UserName

    def GetAge(self):
        return self._Age


def main():
    user1 = User("Julio", 26)
    print(user1.GetUserName())
    print(user1.GetAge())


if __name__ == "__main__":
    main()
