"""
Assignment: Compare Arrays
Write a program that compares two lists and prints a message depending on if
the inputs are identical or not.

Your program should be able to accept and compare two lists: list_one and list_two.
If both lists are identical print "The lists are the same".
 If they are not identical print "The lists are not the same."
"""

def CompareArrays(a, b):
    print ("  list_one = {0}".format(a))
    print ("  list_two = {0}".format(b))
    if (len(a) != len(b)):
        print("    The lists not are the same.  (Length)")
        print(" ")
        return;
    for index in range(0, len(a)):
        if a[index] != b[index]:
            print("    The lists not are the same.  (Content)")
            print(" ")
            return;
    print "    The lists are the same."
    print(" ")
    return;

"""
Try the following test
cases for lists one and two:
"""
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
CompareArrays(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
CompareArrays(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
CompareArrays(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
CompareArrays(list_one, list_two)
