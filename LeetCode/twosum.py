def twosum(self, nums: list[int], target: int) -> list[int]:
    num = len(nums)  # 取List長度,用於List[]取值
    for i in range(num - 1):  # num = 3 : range(0, 3-1 ) = (0,2) 從 0 開始 1 結束
        for j in range(i+1, num):  # i 從 0 開始，j 由 1開始到 List最後
            # print(nums[i], ' + ', nums[j], ' = ',  nums[i]+nums[j]
            if nums[i] + nums[j] == target:
                return [i, j]


# 進階範例
def twosum2(self, nums: list[int], target: int) -> list[int]:
    numMap = {}
    n = len(nums)
    print(numMap)
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i
        print('numMap = ', numMap)
    # return []  # No solution found


# LeetCode input
n1 = [2, 7, 11, 15]
print(twosum(0, n1, 9))

n1 = [3, 2, 4]
print(twosum(0, n1, 6))

n1 = [3, 3]
print(twosum(0, n1, 6))


# n1 = [3, 2, 4]
# print('return = ', twosum1(0, n1, 6))
