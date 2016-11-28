import random

def search(list_, num):
    """Search for num in list_, return True if found."""
    for i in list_:
        if i == num:
            return True
    return False

def bin_search(list_, num):
    """Search for num in list_, return True if found."""
    if len(list_) == 0:
        return False
    if list_[len(list_)//2] > num:
        return bin_search(list_[:len(list_)//2], num) 
    elif list_[len(list_)//2] < num:
        return bin_search(list_[len(list_)//2+1:], num)
    else:
        return True

if __name__=="__main__":
    a = sorted([random.randint(0, 100) for i in range(50)])
    b = random.randint(0, 100)

    print("List: {}".format(a))
    print("Number: {}".format(b))
    print("Naive Search: {}".format(search(a, b)))
    print("Binary Search: {}".format(bin_search(a, b)))