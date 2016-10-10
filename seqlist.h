#include <stdio.h>
#include <stdlib.h>
typedef int Type;
typedef struct 
{
	Type *data;
	int max;
	int size;
}seqlist;

void inilist(seqlist *l,int n);	//准构造函数
void freelist(seqlist *l);	//准析构函数
void insertrear(seqlist *l,Type item);	//尾插
void insert(seqlist *l, int id,Type item);
void erase(seqlist *l,int id);
void clear(seqlist *l);

Type getdata(const seqlist *l, int id);
int size(const seqlist *l);
int empty(const seqlist *l);
int full(const seqlist *l);





