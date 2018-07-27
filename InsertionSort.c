#include<stdio.h>
#include<stdlib.h>

void insertion_sort(int arr[], int num);

int main(){
    int num_elements;
    printf("Enter number of elements:");
    scanf("%d", &num_elements);

    int arr_nums[num_elements];

    printf("Enter the elements:\n");
    int i;
    for(i=0; i<num_elements; i++){
        scanf("%d", &arr_nums[i]);
    }

    insertion_sort(arr_nums, num_elements);

    for(i=0; i<num_elements; i++){
        printf("%d\n", arr_nums[i]);
    }
}

void insertion_sort(int arr[], int num){
    
    int i, value, hole;
    for(i=1; i<num; i++){
        
        value = arr[i];
        hole = i;

        while( (hole>0) && (arr[hole-1]>value) ){
            arr[hole] = arr[hole-1];
            hole--;
        }

        arr[hole] = value;
    }
}