class Operations:
    def sum(self, n1, n2):
        return n1 + n2

    def div(self, n1, n2):
        return n1/n2


class MultiOperations(Operations):
    def mul(self, n1, n2):
        return n1 * n2


def main():
    multiOP = MultiOperations()
    print("2 * 5 = {}".format(multiOP.mul(2, 5)))
    print("2 + 5 = {}".format(multiOP.sum(2, 5)))


if __name__ == "__main__":
    main()
