#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>

void *show(void *s)
{
int sum=0; 
 int a=(int )s;

 for(int i=a;i<a+100;i++)
 {
  sum+=i;
 }

 return (void *)sum;

}
int  main()
{
int *ary[10];
int result=0,j=0;
pthread_t tid[10];
for(int i=0;i<10;i++)
{
tid[i]=i;
}
for(int i=1;i<1000;i+=100)
{
pthread_create(&tid[j],NULL,&show,(void *)i);
j++;
}

for(int i=0;i<10;i++)
{
pthread_join(tid[i],(int *)&ary[i]);

}

for(int i=0;i<10;i++)
{
result+=(int)ary[i];
printf("%d\n",ary[i]);
}

printf("\nsum=%d\n",result);

return 0;

}

