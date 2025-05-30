#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

// solved task number 73

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<int> r, c;
        int i, j;
        for(i=0; i<matrix.size(); i++){
            for(j=0; j<matrix[i].size(); j++){
                if(matrix[i][j] == 0){
                    r.push_back(i);
                    c.push_back(j);
                }
            }
        }
        for(i=0; i<r.size(); i++){
            for(j=0; j<matrix[0].size(); j++){
                matrix[r[i]][j] = 0;
            }
        }
        for(i=0; i<matrix.size(); i++){
            for(j=0; j<c.size(); j++){
                matrix[i][c[j]] = 0;
            }
        }
    }
};

int minutes(int sec){return sec/60;}

int task14_15(){
    int N;
    cout << "How many hours passed? - ";
    cin >> N;
    int hours = N/3600;
    int seconds = N - hours*3600;
    string choice;
    cout << "Do you want to know minutes(m) or seconds(s) remaining?";
    cin >> choice;
    if (choice == "m"){
        cout << "Remaining minutes: "<< minutes(seconds) << endl;
    }else{
        cout << "Remaining seconds: " << seconds << endl;
    }
    return 0;
}

int task12(){
    int passed;
    int failed;
    cout << "How many passed the exam: ";
    cin >> passed;
    cout << "How many failed: ";
    cin >> failed;
    int res = passed + failed;
    cout << "Approximately " << ((float)passed/(float)res)*100 << "% of students passed.\n";
    cout << "Approximately " << ((float)failed/(float)res)*100 << "% of students failed.\n";
    return 0;
}

int task13(){
    int val;
    cout << "Enter value: ";
    cin >> val;
    for (int i=0; i<3; i++){
        cout << val%10 << " ";
        val /= 10;
    }
    return 0;
}

int task11(){
    int salary = 100;
    float sale = (float)salary * 0.05;
    int sales;
    int months;
    cout << "Enter the amount of sales: ";
    cin >> sales;
    cout << "Enter the amount of worked months: ";
    cin >> months;
    cout << "Total salary: "<<(months*salary)+(sale*sales);
    return 0;
}

int task10(){
    int tenge;
    float dollar, euro, ruble;
    cout << "Enter amount in tenge: ";
    cin >> tenge;
    cout << "Enter the cost of dollar to tenge: ";
    cin >> dollar;
    cout << "Enter the cost of euro to tenge: ";
    cin >> euro;
    cout << "Enter the cost of ruble to tenge: ";
    cin >> ruble;
    cout << "You can buy " << (float)tenge/(float)dollar << " in dollars"<<endl;
    cout << "You can buy " << (float)tenge/(float)euro << " in euros"<<endl;
    cout << "You can buy " << (float)tenge/(float)ruble << " in rubles"<<endl;
    return 0;
}

int task9(){
    int val;
    cout << "Enter value: ";
    cin >> val;
    int div = 100;
    for (int i =0; i<3; i++){
        cout << val/div << " ";
        val = val%div;
        div /= 10;
    }
    return 0;
}

int task8(){
    int m;
    int n;
    cout << "Price of an apple: ";
    cin >> n;
    cout << "Asan has: ";
    cin >> m;
    cout << "Asan can buy "<<m/n<<" apples."<<endl;
    return 0;
}

int task7(){
    int hours;
    int minutes;
    int seconds;
    cout << "How many hours?-";
    cin >> hours;
    cout << "How many minutes?-";
    cin >> minutes;
    cout << "How many seconds?-";
    cin >> seconds;
    cout << "Resulting seconds: "<<(3600*hours)+(60*minutes)+seconds<<endl;
    return 0;
}

int task6(){
    float d;
    float pi = 3.14;
    cout << "Enter diameter: ";
    cin >> d;
    cout << "The area is: " << pi*((d*d)/4) << endl;
    cout << "The circumference is: " << 2*pi*(d/2) << endl;
    return 0;
}

int task5(){
    int a;
    int b;
    cout << "Enter width: ";
    cin >> b;
    cout << "Enter length: ";
    cin >> a;
    cout << "The area is "<<a*b << endl;
    cout << "The perimeter is "<<2*(a+b);
    return 0;
}

int task4(){
    int total;
    int grade = 0;
    for (int i=0; i<5; i++){
        cout << "Enter the grade for pupil " << i+1 <<": ";
        cin >> total;
        grade = grade + total;
    }
    float answer = grade/5;
    cout << "The mean grade is: " << answer;
    return 0;
}

int task3(){
    int num;
    cout << "Input number: ";
    cin >> num;
    if (num/100 > 0){
        cout << "Too big number";
        return 0;
    }
    int count = 0;
    for (int i = 0; i<2; i++){
        count = count + num%10;
        num = num/10;
    }
    cout << "Sum of numbers is: "<<count;
    return 0;
}

int task2(){
    int kilos;
    cout << "Input kilos: ";
    cin >> kilos;
    float answer = float(kilos)/(float)1000;
    cout << "The answer is:" << answer << " tonns.";
    return 0;
}

int task1(){
    int centimeters;
    cout << "Input length in centimeters: ";
    cin >> centimeters;
    float answer = (float)centimeters/(float)100;
    cout << "The answer is:" << answer << " meters";
    return 0;
}

int main(){
    //task1();
    //task2();
    //task3();
//    task4(); //to fix mistake
    //task5();
    //task6();
    // task7();
    // task8();
    // task9();
    // task10();
    // task11();
    // task12();
    // task13();
    // task14_15();
    return 0;
}
