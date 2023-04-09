# lets try this patter
# ****1****
# ***222***
# **33333**
# *4444444*
# 555555555

# lets divide the pattern into thre traingles, the first part is the stars, the second part is the numbers and the third part is the stars again.
def main():
    n = 5;
    i = 0;
    j = 0;
    for i in range(n):
        # print the first part of the pattern
        stars = n-i-1;
        for j in range(stars):
            print('*', end='');
        # print the second part of the pattern
        numbers = 2*i+1;
        for j in range(numbers):
            print(i+1, end='');
        # print the third part of the pattern
        for j in range(stars):
            print('*', end='');
        #print a new line
        print('');

# call for the function created above  
if __name__ == '__main__':
    main();