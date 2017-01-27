#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    
    double num,  flag = 0, repeat, i;
    double fib0 = 0, fib1 = 1, fib = fib0 + fib1;
    
    scanf("%lf",&repeat);   
    
    
   
        for(i=0; i<repeat; i++)
            {
                scanf("%lf",&num);
            flag = 0;
            fib0 = 0;
            fib1 = 1;
            fib = fib0 + fib1;
            if(num == 0)
               flag = 1;
            else{
    while(fib <= num)
    {
        if(fib == num)
        {
            flag = 1;
            // break;
        }
        fib0 = fib1;
        fib1 = fib;
        fib = fib0 + fib1;
          
    }
        if(flag == 1)
            printf("IsFibo\n");
        else
            printf("IsNotFibo\n");
    }
    
}
    
    return 0;
}