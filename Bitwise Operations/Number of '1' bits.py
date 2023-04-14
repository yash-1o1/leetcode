# 191
# find number of '1' bits in a binary representation of a number
# Example 1:
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

def main(n: int) -> int:
    count = 0;
    while n != 0:
        if n&1:
            count = count + 1;
        n = n >> 1;
    return count;

# call for the function created above
if __name__ == '__main__':
    print(main(0b1011));