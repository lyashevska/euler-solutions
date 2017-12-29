#include <stdio.h> 

int main(){
    int i = 2, j;
    long x = 600851475143; 

    for (j=1; j<=x; j++){
        if(x%i==0){
            x=x/i;
        } else {
            i++;
            }
        }
    printf("%d \n",x);  
    return 0;
}
