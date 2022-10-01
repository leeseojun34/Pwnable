#include <stdio.h>
#include <stdlib.h>
 
int main(void)
{
    int* heap1;
    int* heap2;
    int* heap3;
 
    heap1 = (int*)malloc(256);
    heap2 = (int*)malloc(256);
 
    printf("heap1 : %p\n",heap1);
    printf("heap2 : %p\n",heap2);
 
    *heap2 = 1234;
    printf("heap2 number : %d\n",*heap2);
 
    free(heap2);
    printf("free heap2\n");
 
    heap3 = (int*)malloc(256);
    printf("new heap : %p\n",heap3);
    printf("new heap number: %d\n",*heap3);
 
    return 0;
}