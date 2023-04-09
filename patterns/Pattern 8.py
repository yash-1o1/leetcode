# lets try to solve a little more complex pattern
# 1234554321
# 1234**4321
# 123****321
# 12******21
# 1********1

# lets divide the pattern into three traingles again, the first part is the numbers, the second part is the stars and the third part is the numbers again.
def main():
    n = 5;
    i = 0;
    j = 0;
    for i in range(n):
        # print the first part of the pattern
        numbers = n-i;
        for j in range(numbers):
            print(j+1, end='');
        # print the second part of the pattern
        stars = 2*i;
        for j in range(stars):
            print('*', end='');
        # print the third part of the pattern
        for j in range(numbers):
            print(n-i-j, end='');
        #print a new line
        print('');

# call for the function created above
if __name__ == '__main__':
    main();