# 1281. subtract the product and sum of digits of an integer
# Example 1:
# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15

# solution for the above problem
def main(n):
    product = 1;
    sum = 0;
    while n != 0:
        digit = n % 10;
        product = product * digit;
        sum = sum + digit;
        n = n // 10;
    return product - sum;

# call for the function created above
if __name__ == '__main__':
    print(main(234));