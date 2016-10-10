#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#define spa '\t'
#include <iostream>
typedef struct
{
	int suit;	//四种花色
	int pips;	//十三种大小
}card;
void shuffle(card *a);
void display(card *a);
int main()
{
	card deck[52];
	int i;
	for(i=0;i<52;i++)
	{
		deck[i].suit=i/13+3;
		deck[i].pips=i%13+1;
	}
	printf("before shuffle:\n");
	display(deck);
	shuffle(deck);
	printf("after shuffle:\n");
	display(deck);
	return 0;
}

void shuffle (card *a )
{
	int i,j;
	card temp;
	srand(time(NULL));
	for(i=0;i<52;i++)
	{
		j=rand()%13;
		temp=a[j];
		a[j]=a[i];
		a[i]=temp;
	}

}

void display(card *a)
{
	int i;
	for (i=0;i<52;i++)
	{
		printf("(%d%3d)",a[i].suit,a[i].pips);
		if ((i+1)%13==0)
			printf("\n");
	}
}
