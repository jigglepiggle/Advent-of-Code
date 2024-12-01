def findDifference(left, right, tot = 0):
    # sort lists from smallest to largest
    left.sort()
    right.sort()

    # find difference
    for i in range(len(left)):
        diff = right[i] - left[i]
        # correct for negativity
        if diff < 0:
            diff *= -1
        # total the difference
        tot = tot + diff

    return tot

def findSimilarity(left, right, tot = 0):
    for i in range(len(left)):
        # count number of occurences of left[i] in right
        c = right.count(left[i])
        # total the number of occurences multiplied by left[i]
        tot = tot + (left[i] * c)

    return tot

# Driver code
left  = []
right = []

with open("input.txt", "r") as f:
    for line in f:
        # Extract data from input.txt, cleanup, and cast to int for later use
        data = list(map(int, line.replace("\n", "").split("   ")))
        # split left and right side of data into seperate lists
        left.append(data[0])
        right.append(data[1])

print(f'Difference: {findDifference(left, right)}')
print(f'Similarity: {findSimilarity(left, right)}')