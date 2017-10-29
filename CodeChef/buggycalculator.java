//Working! :) ....but only sample test cases are available cause the competition got over :|

//https://www.codechef.com/LTIME53/problems/BUGCAL
//Problem Code: BUGCAL

import java.util.*;

class buggycalculator{

    public static void main(String args[]){

        Scanner read_int = new Scanner(System.in);

        int no_tests = read_int.nextInt();
        
        for(int i=0; i<no_tests; i++){
            int x = read_int.nextInt();
            int y = read_int.nextInt();

            int temp_x = x;
            int temp_y = y;

            int sum=0;
            int div = 10;
            int mul = 0;
            while( (temp_x != 0) || (temp_y != 0) ){
               
                if(mul == 0){
                    sum += (temp_x % 10) + (temp_y % 10);
                    mul = 10;
                }
                else{
                    sum += (mul) * ((temp_x % 10) + (temp_y % 10));
                }
                

                temp_x /= 10;
                temp_y /= 10;

                sum %= div;
                div *= 10;
            }

            System.out.println(sum);
        }
    }
}