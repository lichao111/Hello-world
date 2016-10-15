#include <stdio.h>

double light(int *a,int *size)
{
	int i,j;
	for(i=0;i<*size-1;i++)
		for(j=i+1;j<*size;j++)
		{
			if(a[i]>a[j])
			{
				int tem;
				tem=a[i];
				a[i]=a[j];
				a[j]=tem;
			}
		}
	double max=0;
	for(i=0;i<*size-1;i++)
		if(max < (a[i+1]-a[i]))
			max=(a[i+1]-a[i]);
	return max;
}

int main()
{
	int n,l;
	scanf("%d %d",&n,&l);
	int i,a[n];
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	double max=light(a,&n);
	if(a[0]>0&&2*a[0]>max)
		max=2*a[0];
	if(a[n-1]<l&&2*(l-a[n-1])>max)
		max=2*(l-a[n-1]);
	printf("%.2f",max/2.0);
	return 0;
}
