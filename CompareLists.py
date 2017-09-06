def CompareLists(list1, list2):
    print "Input 1: ", list1
    print "Input 2: ", list2
    #None's
    if (None == list1) and (None == list2):
        print "  Identical: Both lists are None, and thus are identical"
        return
    if (None == list1):
        print "  Different:  Null list 1 is smaller than populated list2"
        return
    if (None == list1) and (None == list2):
        print "  Different:  populated list 1 is larger than None list2"
        return
    #Count differences.
    if (len(list1) != len(list2)):
        print "  Different:  Lists are different lengths."
        return
    #Element Differences.
    for k in range(0, len(list1) ):
        print "Index:", k
        if (list1[k] != list2[k]):
            print "  Different:  Values at position {} is different.  '{}' != '{}'".format(k, list1[k], list2[k])
            return
    #the elements match
    print "  Identical: Lists are the same."

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
CompareLists(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
CompareLists(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
CompareLists(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
CompareLists(list_one, list_two)
