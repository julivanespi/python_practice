class User:
    def SetUserName(self, userName):
        self._UserName = userName

    def GetUserName(self):
        return self._UserName


def main():
    user1 = User()
    user1.SetUserName("Julio")
    print(user1.GetUserName())


if __name__ == "__main__":
    main()
