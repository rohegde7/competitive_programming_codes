// Author of the code: Rohit Hegde - hegde.rohit7@gmail.com (https://www.github.com/rohegde7)
// practice problem

#include<stdio.h> 
#include<stdlib.h>

int move_tower(int n, char source, char temp, char destination){

    if(n == 0){
        return 0;
    }

    //else
    move_tower(n-1, source, destination, temp);

    printf("Disk number %d moved from %c to %c\n", n, source, destination);

    move_tower(n-1, temp, source, destination);
}

int main(){

    int n;
    printf("Enter 'n'\n");
    scanf("%d", &n);

    move_tower(n, 'A', 'B', 'C');

    return 0;
}