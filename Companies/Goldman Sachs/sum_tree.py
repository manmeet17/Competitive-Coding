def check(root):
    if root is None:
        return (0,True)
    lsum=check(root.left)
    rsum=check(root.right)
    if lsum[1]==False or rsum[1]==False or ((lsum[0]+rsum[0])!=root.data and lsum[1]!=True and rsum[1]!=True):
        return (None,False)
    return (root.data+lsum[0]+rsum[0],True)


# your task is to complete this function
# function should return True is Tree is SumTree else return False
def isSumTree(root):
    return check(root)[1]
