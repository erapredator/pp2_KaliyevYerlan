# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def spy_game(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False

nums = [int(x) for x in input("Enter a list of integers: ").split()]
print(spy_game(nums))