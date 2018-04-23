/*
We are given a fixed number(15) of names along with a fixed set of numbers(1-5).
We need to print out all the names in order and besides each name a number from the set in a loop manner.
Ex: Suppose we have 4 names A B C D E and 2 numbers [1,2]
    Output: 
        A 1
        B 2
        C 1
        D 2
        E 1
*/

#include<iostream>
#include<string>

using namespace std;

int main(){

    int no_names = 15;
    int numbers[] = {1,2,3,4};
    string names[15];
    
    for(int i=0; i<no_names; i++){
        getline (cin, names[i]);
    }

    int indicator = 1;
    int index = 0; 

    for(int i=0; i<no_names; i++){
        cout << names[i] << numbers[index] << endl;

        if(index == 0){
            indicator = 1;
        }

        if(index == 3){
            indicator = -1;
        }

        index = index + indicator;
    }

    return 0;
}