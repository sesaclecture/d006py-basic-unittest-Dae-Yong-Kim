def check_even_odd(num):
    if num % 2 == 0:
        return True
    return False

def get_avg(nums):
    len_nums = len(nums)
    if len_nums > 0:
        return sum(nums) / len_nums
    return None

def get_max(nums):
    len_nums = len(nums)
    if len_nums > 0:
        return max(nums)
    return None

def get_min(nums):
    len_nums = len(nums)
    if len_nums > 0:
        return min(nums)
    return None