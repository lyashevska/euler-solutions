#include <stdio.h> 
#include <stdlib.h> 
#define MAXIMUM 4000000 

int main(){ 
    int i = 1, j = 1, tot = 0; 

    while(i < MAXIMUM){ 
        if(i%2==0){ 
            tot+=i; 
        } 
        i=i+j; 
        j=i-j; 
    } 
    printf("The sum of the even-valued elements is %d \n", tot); 
    return 0; 
}
