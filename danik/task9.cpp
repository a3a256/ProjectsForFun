#include <iostream>

int main(){
    int op1 = 50;
    int op2 = 45;
    int op3 = 55;
    int discount1 = 10;
    int discount2 = 8;
    int discount3 = 12;
    int min1, min2, min3;
    int wmin1, wmin2, wmin3;
    std::cout << "Minutes during weekdays for operator 1: ";
    std::cin >> min1;
    std::cout << "\nTotal price for weekdays " << min1*op1;
    std::cout << "\nMinutes during weekdays for operator 2: ";
    std::cin >> min2;
    std::cout << "\nTotal price for weekdays for operator 2: " << min2*op2;
    std::cout << "\nMinutes during weekdays for operator 3: ";
    std::cin >> min3;
    std::cout << "\nTotal price for weekdays for operator 3: " << min3*op3;
    std::cout << "\nMinutes during weekends for operator 1: ";
    std::cin >> wmin1;
    std::cout << "\nTotal price for weekends " << (float)wmin1*(float)op1*((float)(100-discount1)/100);
    std::cout << "\nMinutes during weekends for operator 2: ";
    std::cin >> wmin2;
    std::cout << "\nTotal price for weekends for operator 2: " << (float)wmin2*(float)op2*((float)(100-discount2)/100);
    std::cout << "\nMinutes during weekends for operator 3: ";
    std::cin >> wmin3;
    std::cout << "\nTotal price for weekends for operator 3: " << (float)wmin3*(float)op3*((float)(100-discount3)/100);
}