#include <stdio.h>
#include <stdlib.h>

int main()
{
    int r,c,i,j;
    int c1,c2,c3,c4;
    int sum = 0;

    printf("Enter number of rows:");
    scanf("%d",&r);

    int *arr = (int *)malloc(r * r * sizeof(int));
    
    for (i=0; i < r; i++)
    {
        for (j=0; j < r;j++)
        {
            printf("Enter arr[%d][%d]:",i,j);
            scanf("%d",(arr + i * r + j));
        }
    }

    for (i=0; i < r; i++)
    {
        printf("\n");
        for (j=0; j < r;j++)
        {
             printf("%d ",*(arr + i * r + j));
        }
    }
  
    printf("\n");

    for (i=0;i<r;i++)
    {
        for (j=0;j<r;j++)
        {
            sum = sum + *(arr+i*r+j);
        }
    }

    for (i=1;i<r-1;i++)
    {
        for (j=1;j<r-1;j++)
        {
            sum = sum - *(arr+i*r+j);
        } 
    }


    printf("Sum of Edge Elements=%d\n",sum);
}
