def parentheses(s):
    parList = list(s) # convert input string to list, served as stack
    unpairedLeftCount = 0
    unpairedRightCount = 0
    while parList:  # iterate over each symbol in the string
        curPar = parList.pop(0)
        if curPar == ')':
            if unpairedLeftCount > 0:  # paired with an existing (
                unpairedLeftCount -= 1
            else:
                unpairedRightCount += 1 # pairing failure
        else:
            unpairedLeftCount += 1  # add to queue waiting for next ) to pair
    return unpairedLeftCount + unpairedRightCount

def parentheses_simple(s):
    parDict = {'(':1, ')':-1}
    unpairedLeftCount = unpairedRightCount = 0
    for c in s:  # iterate over each symbol in the string
        unpairedLeftCount = max(0, unpairedLeftCount + parDict[c])
        unpairedRightCount += 0**unpairedLeftCount # 0**0 = 1, otherwise = 0 
    return unpairedLeftCount + unpairedRightCount

def distinct_subarray(arr, k):
    freqDict = {}
    leftBound = 0
    rightBound = -1
    minLength = len(arr) + 1
    while rightBound < len(arr) - 1:
        while len(freqDict) < k and rightBound < len(arr) - 1:
            rightBound += 1
            if arr[rightBound] in freqDict.keys():
                freqDict[arr[rightBound]] += 1
            else:
                freqDict[arr[rightBound]] = 1
        if len(freqDict) == k:  # only change min value if such sub array exists 
            minLength = min(minLength, rightBound - leftBound + 1)
        while len(freqDict) >= k and leftBound < rightBound:            
            freqDict[arr[leftBound]] -= 1
            if freqDict[arr[leftBound]] == 0:
                freqDict.pop(arr[leftBound], None)
            leftBound += 1
        if minLength <= len(arr): # only change min value if such sub array exists
            minLength = min(minLength, rightBound - leftBound + 2)
    if minLength <= len(arr):
        return minLength
    else:
        return -1


print(distinct_subarray([2, 2, 1, 1, 3], 4))
