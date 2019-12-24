def reverse_string():
    string = input("Enter a long string: \n").split()
    string.reverse()
    s = " ".join(string)
    return s


print(reverse_string())
