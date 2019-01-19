# Writing a small program

def CountingToEleven():
    count = 1
    # Code block 1
    while count < 11 :
        print(count)

        
        count = count + 1
    # Code block 2
    if count == 11 :
        print("Counting Complete")


if __name__ == '__main__':
    CountingToEleven()