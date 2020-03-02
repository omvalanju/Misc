#include<stdio.h>

struct employee {
    char name[100];
    int number;
    int salary;
};


int main() {
    int size;
    struct employee e;
    
    size = sizeof(e);
    printf("%d", size);
    
    return(0);
}
