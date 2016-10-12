#include <stdio.h>
void selectsort(int *a,const int size);
void display(const int *a,const int size);
int findsamll(const int *a,const int size);
void insersort( int *a, int size);
void bubblesort(int *a,int size);
void shellsort(int *a, int size);
int main()
{
	int a[10]={10,1,2,4,7,8,3,9,5,6};
	display(a,10);
	printf("the samllest tumple is:%d\n",findsamll(a,10));
	selectsort(a,10);
	printf("after selectsort,a[]:");
	display(a,10);
	int b[10]={10,9,8,7,2,3,5,4,1,6};
	printf("after insersort,b[]:");
	insersort(b,10);
	display(b,10);
	int c[10]={18,29,30,38,8299,267,378,29,83,0};
	printf("after bubblesort,c[]:");
	bubblesort(c,10);
	display(c,10);
	return 0;
}


int findsamll(const int *a,const int size)
{
	int i,min=a[0];
	for(i=1;i<size;i++)
	{
		if(a[i]<min)
			min=a[i];
	}
	return min;
}

void display(const int *a,const int size)
{
	int i=0;
	for(;i<size;i++)
		printf("%d\t",*(a+i));
	printf("\n");
}

void selectsort(int *a,const int size)	//选择排序，把数组分成两部分，左边已排序，右边未排序，每次从未排序部分选择最小的一次放在左边 时间复杂度O(n^2)
{
	int i,j;
	for(i=0;i<size;i++)
	{
		int min_index=i;
		int temp;
		for(j=i+1;j<size;j++)
			if(a[j]<a[min_index])
				min_index=j;
		temp=a[i];
		a[i]=a[min_index];
		a[min_index]=temp;
	}

}

void insersort(int *a,int size)//从第二个元素开始进行循环，给它在左边找合适的位置，找比他大的，找到后放在该元素前面（要先全部右移)时间复杂度O(n^2)
{
	int i,j;
	for(i=1;i<size;i++)
	{
		int temp=a[i];
		for(j=i-1;j>=0;j--)
		{
			if(temp>=a[j])
				break;
			else
			{
				a[j+1]=a[j];
				a[j]=temp;
			}		
		}
	}
}

void bubblesort(int *a, int size)//依次比较相邻的元素，前者大则交换，时间复杂度O(n^2)
{
	int i,j;
	for(i=0;i<size-1;i++)
		for(j=i+1;j<size;j++)
			if(a[i]>a[j])
			{
				int temp=a[j];
				a[j]=a[i];
				a[i]=temp;
			}
}

void shellsort(int *a,int size)
{
	
}


