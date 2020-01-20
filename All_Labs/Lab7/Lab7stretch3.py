def reverse(string):
    str = ""
    for i in string:
        str = i + str

    if str == string:
        print (string, "is a palindrome")

    else:
        print (string, "is not a palindrome")
