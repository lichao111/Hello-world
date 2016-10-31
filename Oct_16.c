#include <stdio.h>
void func1(int &c)
{
	printf("%d\n",c);
}

void func2(int *c)
{
	printf("%p\n",c);
}
union b
{
	int i;
	char x[2];
};
int main()
{
	union b a;
	a.x[0]=10;
	a.x[1]=1;
	printf("%d\n%d\n%d",a.i,a.x[0],a.x[1]);
}
