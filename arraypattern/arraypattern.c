#include <stdio.h>
#include <stdlib.h>

int main()
{
    int r,n,i,j,k,x,y,tmp;

    printf("Enter Number:");
    scanf("%d",&n);

    r = n + (n - 1);

    int *arr = (int *)malloc(r * r * sizeof(int));

    for (i=0;i<r;i++)
    {
        for (j=0;j<r;j++)
        {
            *(arr + i * r + j)=n;
        }
    }

    x = 1;
    y = 1; 

    for (k=r;k>0;k--)
    {
        for (i=x;i<k-1;i++)
        {
            for (j=y;j<k-1;j++)
            { 
                *(arr+i*r+j)=*(arr+i*r+j)-1;
            }
        }
        x = x + 1;
        y = y + 1;
    }

    for (i=0; i < r; i++)
    {
        for (j=0; j < r;j++)
        {
             printf("%d ",*(arr + i * r + j));
        }
        printf("\n");
    }

}
