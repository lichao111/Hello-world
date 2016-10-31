#include <stdio.h>

typedef struct Node
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
}

int main()
{
	return 0;
}
