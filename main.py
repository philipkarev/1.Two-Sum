class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if int(nums[i]) + int(nums[j]) == int(target):
                    print("Result:", i, "and", j)
                    return [i, j]

        return []

def main():

    print("Enter nums (no any symbols, just numbers):")
    nums = list(input())
    print("Enter target:")
    target = input()

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if int(nums[i]) + int(nums[j]) == int(target):
                print("Result:", i, "and", j)
                return [i, j]

    print("No result")


main()