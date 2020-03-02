#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main()
{
    char str[10];
    scanf("%s",str);
    
    if (isdigit(str))
    {
        printf("Number");
    }
    return 0;
}
