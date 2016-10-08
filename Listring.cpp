#include <iostream>
#include <stdio.h>

using namespace std;
unsigned int Lstrlen(const char *a);

int main()
{
	char a[]="China";
	printf("%d\n",Lstrlen(a));

	return 0;
}

unsigned int Lstrlen(const char *a)
{
	unsigned int len=0;
	int j;

	for (j=0;*(a+j)!='\0';j++)
	{
		printf("%x\n",*(a+j));
		len++;
		printf("%d\n",len);
	}
	return len;

}
