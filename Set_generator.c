#include <stdio.h>
#include <math.h>
#define N 9

void print_binary_n_digits(unsigned int num, int n) {
    int i;
    // Loop from the most significant bit position to the least significant
    for (i = n - 1; i >= 0; i--) {
        // Use bitwise right shift (>>) and bitwise AND (& 1) to check the bit at position 'i'
        int digit = (num >> i) & 1; 
        printf("%d", digit);
    }
}

int majority_bit(unsigned int x, int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        count += (x >> i) & 1;
    }
    return (count > n / 2) ? 1 : 0;
}

int main() {
    int digits = N;
    printf("[");
    for(unsigned int i = 0; i < pow(2,digits); i++) {
        if(majority_bit(i, digits) == 0) {
            if(i != 0) {
                printf(",");
            }
            printf("\"");
            print_binary_n_digits(i, digits);
            printf("\"");
        }
    }
    printf("]");
    return 0;
}
