def digit_sum(num):
    total = 0

    for digit in str(num):
        total += int(digit)

    return total


def minimum_digit_sum(nums):
    result = []

    for num in nums:
        result.append(digit_sum(num))

    return min(result)


# Contoh penggunaan
print(minimum_digit_sum([10, 12, 13, 14]))  # 1
print(minimum_digit_sum([1, 2, 3, 4]))      # 1
print(minimum_digit_sum([999, 19, 199]))    # 10
