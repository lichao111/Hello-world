#include <stdio.h>
extern void B();
void A()
{
	putchar("A");
	B();
}
