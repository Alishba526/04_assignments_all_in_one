MAX_LENGTH = 3  # Required by autograder

def shorten(lst):
    """Removes and prints items from the end of the list until its length is MAX_LENGTH."""
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()       # remove last element
        print(removed)            # print it

def get_lst():
    """Prompts the user to enter elements for the list."""
    lst = []
    elem = input("Enter a value (or press enter to finish): ")
    while elem != "":
        lst.append(elem)
        elem = input("Enter a value (or press enter to finish): ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)

if __name__ == '__main__':
    main()
