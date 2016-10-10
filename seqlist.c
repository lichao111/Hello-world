#include <stdio.h>
#include <stdlib.h>
#include "seqlist.h"

typedef int Type;
int main()
{
	int i,n;
	seqlist L;
	inilist(&L,10);
	insertrear(&L,8);
	insertrear(&L,15);
	insertrear(&L,20);
	insert(&L,1,90);
	n=size(&L);
	for (i=0;i<n;i++)
		printf("%d\t",getdata(&L,i));
	clear(&L);
	freelist(&L);
	return 0;
}

void inilist(seqlist *l, int n)
{
	l->data=(Type*)malloc(n*sizeof(Type));
	if (l->data=NULL)
	{
		printf("memory allocation error\n");
		exit(1);
	}
	l->size=0;
	l->max=n;
}

void freelist(seqlist *l)
{
	free(l->data);
}

void clear(seqlist *l)
{
	l->size=0;
}
void insertrear(seqlist *l,Type item)
{
	if(l->size=1 > l->max)
	{
		printf("iist in full!");
		exit(1);
	}
	l->data[l->size]=item;
	l->size++;
	l->size = l->size +1;

}
void insert(seqlist *l, int id, Type item)
{	
	if (l->size+1 > l->max || id >l->size ||id <0)
	{	printf("list is full or id is illegal!");
		exit(1);
	}
	int i;
	for(i=l->size-1;i>=id;i--)
		l->data[i+1]=l->data[i];
	l->data[id]=item;
	l->size++;
}
int size(const seqlist *l)
{
	return l->size;
}

Type getdata (const seqlist *l, int id)
{
	return l->data[id];
}




	




