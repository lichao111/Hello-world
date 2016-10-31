int unique(int **arrays, int *array_size)
{
	int len=0,i=0,j=0,k=0;
	while(i<10)
	{
		len += array_size[i++]
	}
	int *p= (int *)malloc(len*sizeof(int));
	for(i=0;i<10;i++)
		for(j=0;j<arrayz_size[i];j++)
		{
			*p[k++]= arrays[i][j]
		}
	for(i=0;i<len;i++)
		for(j=i+1;j<len;j++)
			if(*p[i]>*p[j])
			{
				int temp;
				temp=a[j];
				a[j]=a[i];
				a[i]=temp;
			}
	int uq=0;
	while(i<len&&a[i]![i+1])
	{
		uq++;
		i++;
	}	
	return uq;
}
