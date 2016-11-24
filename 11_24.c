#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main();
void f(char **p){
    char *t;
	printf("%ld\n",sizeof(int));
    char *q;
	q=(p+sizeof(int))[0];
	printf("%s\n",q);
	t=(p+sizeof(int))[-1];
    
	printf("%s\n",t);
}

void f2(int *p){
	printf("%p\n",p);
	p=p+3;
	printf("%p\n",p);
	printf("%d,",*p);
}
int main(){
    /*char *arg[]={"ab","cd","ef","gh","ij","kl"};
    f(arg);
	printf("=========\n");
	int a[5]={1,2,3,4,5},*r=a;
	printf("%p\n",r);
	printf("%d\n",*r);
	int *p=r;
	printf("%d\n",*p);
	printf("%p\n",p);
	f2(r);
	printf("%p\n",r);
	printf("%d\n",*r);
	char u[]="abc";
	printf("%s\n",u);
	int h=0x123-123;
	printf("%d\n",h);
	int y='\x12'+'\012'+'\0'+'0';
	printf("%d",y);
	int l='\x12';
	printf("%d\n",l);
	int z=0x41;
	printf("%c",z);
	char s=0101;
	printf("%c",s);
	char str1[]="I am ";
	char str2[]="Chao";
	strcat(str1,str2);
	printf("%s",str1);*/
	int a[]={1,2,3};
	int *b=a;
	int *c=a;
	int *d=b;
	printf("%p,%p,%p,%p\n",&a,b,c,d);
	d++;
	*d=100;
	*b=1000;
	printf("%d,%d\n",a[0],a[1]);
	return 0;
}
