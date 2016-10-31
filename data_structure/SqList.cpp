#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LIST_INIT_SIZE 100
#define LISTINCREMENT 10
#define Elem int
#define TRUE 1
#define FALSE 0
#define OK 1
#define INFEASIBLE -1
#define OVERFLOW -2

typedef int Status;
typedef struct {//the definition of Sequence List
	Elem * elem;//存储空间的基值   8 bype
	int length;//
	int listsize;// sizeof(int)=4         sizeof(SqList)=8+4+4=16
}SqList;

Status DeleteK(SqList &a, int i ,int k)
{//删除i开始的k个节点
	if(i<0||k<0||i+k>a.length)
		return FALSE;
	else
	{
		while(i+k+1<a.length)
		{
			a.elem[i]=a.elem[i+k];
			i++;
		}
	}
	a.length=a.length-k;
	return OK;
}

Status Display(SqList &a)
{
	int j=0;
	printf("SeList:");
	while(j<a.length)
		printf("%d  ",a.elem[j++]);
	printf("\n");
}

Status InitSqList(SqList &a)
{
	a.elem=(Elem*)malloc(LIST_INIT_SIZE*sizeof(Elem));
	if(!a.elem)
		return OVERFLOW;
	printf("InitSqList:%p\n",a.elem);
	a.length=0;
	a.listsize=LIST_INIT_SIZE;
	return  OK;
}

Status DestroyList(SqList &a)
{
	if(a.elem)//一个malloc对应一个free，ralloc之后还是可以看作用了一次malloc，malloc+ralloc <=> free
	{
//		printf("Destroy:%p\n",a.elem);
		free(a.elem);
		a.length=0;
		a.listsize=0;
	}
	else
		return FALSE;
}
void ClearList(SqList& a)
{
	a.length=0;
}

bool ListEmpty(SqList& a)
{
	if(a.length==0)
		return true;
	else
		return false;
}

Status push_back(SqList &a,Elem e)
{
	if(a.length==a.listsize)
	{
		a.elem=(Elem*)realloc(a.elem,(a.length+LISTINCREMENT)*sizeof(Elem));
		a.listsize += LISTINCREMENT;//增加内存分配以后不要忘了把顺序表的最大空间也作相应的更改
	}
	if(!a.elem)
		return OVERFLOW;
	a.elem[a.length]=e;
	a.length++;
}

int ListLength(SqList& L)
{
	return L.listsize;
}

Status GetElem(SqList& L,int i,Elem &e)
{
	if(i<1||i>L.length)
		return FALSE;
	e=L.elem[i-1];
	return OK;
}

Status PriorElem(SqList &L,Elem &s,Elem e)
{
	int i=0;
	while(L.elem[i]!=e&&i<L.length)
		++i;
	if(i==L.length)
		return FALSE;
	else
	{
		s=L.elem[i-1];
		return OK;
	}
}

Status NextElem(SqList &L,Elem &s,Elem e)
{
	int i=0;
	while(L.elem[i]!=e&&i<L.length-1)
	{
		++i;
	}
	if(i==L.length-1)
	{
		printf("have no next tumple\n");
		return FALSE;

	}
	else
	{
		s=L.elem[i+1];
		return OK;
	}
}

Status ListInsert(SqList &L,Elem cur,Elem next)
{
	if(cur<0||cur>=L.length)
		return FALSE;
	if(L.length==L.listsize)
		L.elem=(Elem*)realloc(L.elem,sizeof(Elem)*(LISTINCREMENT+L.listsize));
	if(!L.elem)
		return OVERFLOW;
	else
		L.listsize += LISTINCREMENT;
	int i=cur-1;
	int j=L.length-1;
	while(j>=i)
	{
		L.elem[j+1]=L.elem[j];
		j--;
	}
	L.elem[i]=next;
	L.length++;
	printf("insert sucess!");
	return OK;
}

bool LocateList(SqList &L, Elem e)
{
	int i=0;
	while(i<L.length)
		if(L.elem[i]==e)
			return 1;
		else
			i++;
	return 0;
}

int main()
{
	SqList L;
	printf("%ld\n",sizeof(L));
	InitSqList(L);
	int i;
	for(i=0;i<20;++i)
		push_back(L,i);
	Display(L);
	printf("L.length :%d\n",L.length);
	printf("listlength:%d\n",ListLength(L));
	Elem e,prio,next;
	GetElem(L,2,e);
	PriorElem(L,prio,e);
	NextElem(L,next,e);
	printf("the number 2 tumple:%d\n",e);
	printf("prio e:%d\n",prio);
	printf("next e:%d\n",next);
	ListInsert(L,8,10000);
	Display(L);
	LocateList(L,10000);
	DeleteK(L,5,3);
	Display(L);
	DestroyList(L);
	printf("size of a.length :%d\n",L.listsize);
	if(ListEmpty(L))
		printf("empty!\n");
	
	/*char* p = NULL;
	p=(char*)malloc(10*sizeof(char));
	if(p==NULL)
	{
		printf("filure");
		exit(1);
	}
	printf("%p\n",p);

	strcpy(p,"abc");
	printf("%c\n%c\n%c\n",*p,*p+1,*p+2);
	printf("%p\n%p\n",p,p+1);
	//if(p!=NULL)
		free(p);
	//p=NULL;
	
	//DestroyList(L);
	//Display(L);*/ return 0;
}
