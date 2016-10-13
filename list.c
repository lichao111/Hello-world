#include <stdio.h>
#include <stdlib.h>
#define Type int

struct Node
{
	Type data;
	struct Node *prev;
	struct Node *next;
};

typedef struct Node Node;

typedef struct
{
	Node *head;
	Node *tail;
	int size;
}List;

void initialLise(List *l)
{
	l-> head=(Node*)malloc(sizeof(Node));	//head和tail虽然有data成员，但是不存储数据。
	if(l->head ==NULL)
	{
		printf("error,exit");
		exit(1);
	}
	l->head->prev =l->head->next=NULL;
	l-> tail=(Node*)malloc(sizeof(Node));
	if(l->tail ==NULL)
	{
		printf("error,exit");
		exit(1);
	}
	l->tail->prev =l->tail->next=NULL;
	l->head->next=l->tail;
	l->tail->prev=l->head;
	l->size=0;

}

Node *begin(List *l)
{
	return l->head->next;
}

Node *end(List *l)
{
	return l->tail->prev;
}

Node *get_node(Type item, Node *prev0,Node *next0)//制作一个节点
{
	Node *p;
	p=(Node*)malloc(sizeof(Node));
	if(p=NULL)
	{
		printf("Memory allocation failure!");
		exit(1);
	}
	p->data=item;
	p->prev=prev0;
	p->next=next0;
	return p;
}

void set_data(Node *current, Type item)
{
	current -> data =item;
}

Node *insert(List *l,Node *current,Type item)	//在current节点的前面插入一个值为item的节点
{
	Node *p=current;
	l->size++;
	p->prev->next=get_node(item, p->prev,p);
	p->prev=p->prev->next;
	return p->prev;
}

Node *erase(List *l,Node *current)
{
	Node *p=current;
	Node *re=p->next;
	p->prev->next=p->next;
	p->next->prev=p->prev;
	free(p);
	l->size--;
	return re;
}
int main()
{
	return 0;

}
