#include <iostream>
#include <math.h>
#include <vector>


std::vector<float> solve(float a, float b, float x, float z){
    float first = a*pow(sin(x), 2) + b*cos(z*x+a);
    float second = pow((a+b*x), 2) - sin(a+z*x);
    float third = sqrt(x-(sin(b*x+z)));
    return {first, second, third};
}

int main(){
    std::vector<float> res;
    float a1 = 1.2f;
    float b1 = 7.2f;
    float x1;
    std::cout << "Enter x: ";
    std::cin >> x1;
    float z1 = exp(x1);
    res = solve(a1, b1, x1, z1);
    std::cout << "\n" << res[0] << " " << res[1] << " " << res[2];
    float a2 = -1.5f;
    float b2 = 3.2f;
    float x2;
    std::cout << "\nEnter x: ";
    std::cin >> x2;
    float z2 = exp(2*x1);
    res = solve(a2, b2, x2, z2);
    std::cout << "\n" << res[0] << " " << res[1] << " " << res[2];
    float a3 = 1.7f;
    float b3 = 5.5f;
    float x3;
    std::cout << "\nEnter x: ";
    std::cin >> x3;
    float z3 = exp(3);
    res = solve(a3, b3, x3, z3);
    std::cout << "\n" << res[0] << " " << res[1] << " " << res[2];
    return 0;
}