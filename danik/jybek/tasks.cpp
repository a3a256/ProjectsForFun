#include <iostream>
#include <iomanip>
#include <string>
#include <string.h>

using namespace std;

int task2(){
    string a = "";
    string* b=&a;
    string inputString;
    cout<<"Enter String:"<<endl;
    getline(cin,inputString);

      //Crete object of istringstream and
      //initialize assign input string
    istringstream iss(inputString);

    string word;
      //Extract each words only..no spaces.
      //This way it can handle any
      //special characters.

    while(iss >> word) {  
            //Display words
            // cout<<word.c_str()<<endl;
            *b = word.c_str();  
    }
    for (int i = 0; i<a.length(); i++){
        char* ch = &a[i];
        *ch = toupper(a[i]);
        // cout << a;
    }
    cout << a;

    return 0;
}


int task1(){
    int number;
    cout << "Enter value: ";
    cin >> number;
    int v = number;
    int val = number;
    string a = "";
    string l = "";
    int count=0;
    while (v>0){
        v = v/1000;
        count ++;
    }
    string arr[count];
    int j = 0;
    while (val>0){
        a = to_string(val%1000);
        if(val/1000 != 0){
            if(a.length()<3){
                int k = a.length();
                for(int i=0; i<(3-k); i++){
                    a = "0"+a;
                }
            }
        }
        val = val/1000;
        arr[j] = a;
        j++;
        a = "";
    }
    string* output=&l;
    for(int i=count-1; i>=0; i--){
        *output += arr[i] + " ";
    }
    cout << l;
    return 0;
}


int main(){
    // task1();
    task2();
    return 0;
}