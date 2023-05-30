#include <iostream>
#include <vector>

class Queue{
    public:
        std::vector<int> arr = {23, 21, 18, 16, 14, 11, 9, 6, 4, 2};

        void push(int val){
            int i;
            for(i=0; i<arr.size(); i++){
                if(val > arr[i]){
                    arr.insert(arr.begin()+i, val);
                    break;
                }
            }
        }

        void print(){
            int i;
            for(i=0; i<arr.size(); i++){
                std::cout << arr[i] << " ";
            }
            std::cout << "\n";
        }
};


int main(){
    Queue q;
    q.push(22);
    q.print();
}