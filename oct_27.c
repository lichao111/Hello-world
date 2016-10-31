#include <stdlib.h>
#include <stdio.h>
#include <iostream>
using namespace std;
#define ElemType int

typedef struct List{
	int  data;
	struct List *next;
}List

void HeadCreatList(List *L)//头插法
{
	List *s;
	L->next=NULL;
	int i=0;
	for(;i<10;i++)
	{
		s=(struct List*)malloc(sizeof(struct List));
		s->data=i;
		s->next=L->next;
		L->next=s;
	}
}

void TailCreatList(List* L)//尾插法
{
	List *s,*r;
	r=L;
	int i=0;
	for(;i<10;i++)
	{
		s=(List*)malloc(sizeof(List));
		s->data=i;
		r->next=s;
		r=s;
	}
	r->next=NULL;
}

void Display(List* L)
{
	List*p=L->next;
	while(p!=NULL)
	{
		printf("%d -> ",p->data);
		p=p->next;
	}
	printf("\n");
}


int main()
{
	//position p=(position)malloc(sizeof(LNode));
	//cout<<sizeof(p)<<endl;
	//p->data=3;
	//cout<<(*p).data<<endl;
	List *L,*s;
	L=(List*)malloc(sizeof(struct List));
	s=(List*)malloc(sizeof(List));
	HeadCreatList( L);
	Display(L);
	TailCreatList(s);
	Display(s);
	
	
	return 0;
}


