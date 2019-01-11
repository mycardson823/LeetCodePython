def power3(n):
    i = 1
    reminder = n
    while reminder > 1 and i < reminder:
        i += 1
        if reminder % (i**3) == 0:
            reminder = reminder / (i**3)
            i = 1
    if reminder == 1:
        return True
    return False
def power33(n):
    from math import log, floor
    power = log(n, 3)
    return power == floor(power)

def removeInPlace(nums, n):
    i, j = 0, 1
    length = 0
    while i < len(nums)-j:
        if nums[i] == n:
            while nums[-j] == n:
                j += 1
            if j == len(nums) - i:
                return
            nums[i] = nums[-j]
            nums[-j] = n
            i += 1
    return len(nums) - j

def reverseNumber(num):
    res = 0
    reminder = abs(num)
    while reminder > 0:
        tail = reminder % 10
        reminder = reminder // 10
        res = 10*res + tail
    return res if num >= 0 else -res


def countPrimeSetBits(self, L, R):
    def getOnes(n):
        count = 0
        while n:
            n &= n-1
            count += 1
        return count

    primeNums = [2]
    for n in range(3, 32):
        isPrime = True
        for pnum in primeNums:
            if n % pnum == 0:
                isPrime = False
        if isPrime:
            primeNums.append(n)
    count = 0
    for num in range(L, R+1):
        if getOnes(num) in primeNums:
            count += 1
    return count


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def dominantIndex(self, nums):
        first, second = -1, -2
        maxIndex = 0
        for i, n in enumerate(nums):
            if n > first:
                second = first
                first = n
                maxIndex = i
            elif n > second:
                second = n
        return maxIndex if first >= 2 * second else -1

    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2

        def mergeLists(list1, list2):
            cur1 = list1
            while cur1.next and cur1.next.val <= list2.val:
                cur1 = cur1.next
            tmp = cur1.next
            cur1.next = list2
            mergeLists(list2, tmp)
            return list1

        if l1.val < l2.val:
            return mergeLists(l1, l2)
        else:
            return mergeLists(l2, l1)


    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.sum = sum
        self.count = 0
        def getSum(root, sum):
            if sum == 0:
                self.count += 1
            rem = sum - root.val
            getSum(root.left, rem)
            getSum(root.right, rem)
            getSum(root.left, self.sum)
            getSum(root.right, self.sum)
        getSum(root, sum)
        return self.count

mySolution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
print(mySolution.mergeTwoLists(l1,l2))
