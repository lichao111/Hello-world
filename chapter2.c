#include <stdio.h>
#include <math.h>
//4.
int jiecheng(int n)
{
	int s=1 ;
	int i;
	for (i=1; i<=n; i++)
	{
		s*=i;
	}
	return s;
}

//5.
int Fibonacci(int n)
{
	int s;
	if(n==1 || n==2)	{s=1;}
	else
		s= Fibonacci(n-1)+Fibonacci(n-2);
	return s;
}
int fib(int n)  
{  
    int result[2] = {0,1};  
    if(n < 2)  
        return result[n];  
    int fibOne = 0;  
    int fibTwo = 1;  
    int fibN   = 0;  
    int i = 0;  
    for(i = 2; i <= n; i++)  
    {  
        fibN = fibOne + fibTwo;  
          
        fibOne = fibTwo;  
        fibTwo = fibN;  
    }  
      
    return fibN;  
}

void zhif()
{
	int x,y,z;
	for (y=0;y<=9;y++)
	{
		for (x=0;x<=10-y;x++)
		{
			if ((((float )10-x-y)==((float)(18-x-2*y)/5))&&((10-x-y)>=0))
			{
			printf("x=%d\ny=%d\nz=%d;\n",x,y,10-x-y);
			}
		}
	}
}

//8.gougu
void gougu()
{
	int i,j,k;
	for (i=3;i<=100;i++)
	{
		for (j=i+1;j<=100;j++)
		{
			for (k=j+1;k<=100;k++)
				if (i*i+j*j==k*k)	
				printf("%d,%d,%d\n",i,j,k);
	
		}
	}
}
int main()
{
	int n;
	printf("please input jiecheng value of the n:");
	scanf("%d",&n);
	printf("the output of %d is %d \n",n,jiecheng(n));
	int j;
	for(j=1;j<=10;j++)
	{
		printf("a%d:%d\n",j,fib(j));}
	zhif();
	gougu();
	return 0;
}
