#include <iostream>
#include <vector>
#include <algorithm>

int main(){

    std::vector<char> arr;
    std::string value = "Hello World! ";
    int i;
    for(i=0; i<value.size(); i++){
        arr.push_back(value[i]);
    }

    std::string res = "";

    for(i=0; i<arr.size(); i++){
        std::cout << arr[i];
        if(arr[i] == ' '){
            res += arr[i];
            res += ' ';
        }else{
            res += arr[i];
        }
    }

    std::cout << "\n" << res << "end\n";


    return 0;
}