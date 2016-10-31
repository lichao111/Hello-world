#include <stdio.h>
#include <stdlib.h>

extern void A();
void B()
{
	putchar("B");
	if (rand()%2 == 1)
		A();
}
