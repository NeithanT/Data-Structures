#include <iostream>
#include <time.h>

int main() {

    int arr[100000];
    long sum = 0;
    long sum2 = 0;

    for(int i = 0; i < 100000; i++) {
        arr[i] = std::rand() % 1000;
    }

    // Time it
    clock_t start = clock();

    for (int i = 0; i < 100000; i++) {
        if (arr[i] > 500) {
            sum += arr[i];
        }
    }

    double elapsed = double(clock() - start) / CLOCKS_PER_SEC;
    std::cout << "Elapsed time: " << elapsed << " seconds" << std::endl;


    start = clock();

    for (int i = 0; i < 100000; i++) {
        int t = (arr[i] - 500) >> 31;
        sum2 += ~t & arr[i];

    }

    elapsed = double(clock() - start) / CLOCKS_PER_SEC;
    std::cout << "Elapsed time: " << elapsed << " seconds" << std::endl;

    std::cout << "\nSum: " << sum << std::endl;
    std::cout << "Sum2: " << sum2 << std::endl;

    // Examples of the left and right shift operator
    int x = 8;  // 0000 1000 in binary
    int y = x << 1;  // Left shift: 0001 0000 (16 in decimal)
    int z = x >> 1;  // Right shift: 0000 0100 (4 in decimal)
    std::cout << "Left shift of " << x << ": " << y << std::endl;
    std::cout << "Right shift of " << x << ": " << z << std::endl;

    // More examples
    int a = 15;  // 0000 1111 in binary
    int b = a << 2;  // Left shift: 0011 1100 (60 in decimal)
    int c = a >> 2;  // Right shift: 0000 0011 (3 in decimal)
    std::cout << "Left shift of " << a << ": " << b << std::endl;
    std::cout << "Right shift of " << a << ": " << c << std::endl;

    // MORE EXAMPLES
    int d = 32;  // 0010 0000 in binary
    int e = d << 3;  // Left shift: 1000 0000 (256 in decimal)
    int f = d >> 3;  // Right shift: 0000 0010 (4 in decimal)
    std::cout << "Left shift of " << d << ": " << e << std::endl;
    std::cout << "Right shift of " << d << ": " << f << std::endl;

    // More examples but with negative values
    int g = -8;  // 1111 1000 in binary (two's complement)
    int h = g << 1;  // Left shift: 1111 0000 (-16 in decimal)
    int i = g >> 1;  // Right shift: 1111 1100 (-4 in decimal)
    std::cout << "Left shift of " << g << ": " << h << std::endl;
    std::cout << "Right shift of " << g << ": " << i << std::endl;

    // More with negative values
    int j = -15;  // 1111 0001 in binary (two's complement)
    int k = j << 2;  // Left shift: 1110 0000 (-60 in decimal)
    int l = j >> 2;  // Right shift: 1111 1100 (-4 in decimal)
    std::cout << "Left shift of " << j << ": " << k << std::endl;
    std::cout << "Right shift of " << j << ": " << l << std::endl;

    return 0;
}