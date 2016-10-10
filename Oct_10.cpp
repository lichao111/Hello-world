#include <iostream>
#include <stdio.h>

typedef struct 
{
	int yr;
	int mh;
	int day;
}H;

typedef union 
{
	int i;
	int j;
	int k;
}L;
//---------字符串基本操作函数------------
unsigned lstrlen(char * a);
char * lstrcpy(char * b, const char *a);
char * lstrcat(char * b, const char *a);
int main()
{
	H l={201,2001,1};
	L s={5};
	printf("%d\n",s.i);
	char a[]="ChaoLi";
	printf("%d\n",lstrlen(a));
	char b[]="";
	char c[]="Hello!";
	printf("%s\n",lstrcpy(b,a));
	printf("%s\n",lstrcat(c,b));
	return 0;
}

unsigned lstrlen(char * a)
{
	unsigned len=0;
	while (* a++ !=0)
		len++;
	return len;
}

char * lstrcpy(char*b,const char *a)
{
	printf("//----------indicator-----------\n");
	char *p =b;
	while( * a!= '\0')
		* p++=*a++;
	* p = '\0';
	return b;
}

char * lstrcat(char  *b, const char *a)
{	
	int lenb=lstrlen(b);
	char *p=b+lenb;
	int i=0;
	while(*a != '\0')
	{
		*(p++)=*(a++);
	}
	*(p)='\0';
	return b;
}






