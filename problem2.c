#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char stack[100];
void push(char);
void pop();
void find_top();
int top = -1;
 
void main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
	int i;
	char a[100];
	scanf("%s", &a);
	for (i=0;a[i]!='\0';i++)
	{
		if (a[i] == '(')
			push(a[i]);
		else if (a[i] == ')')
			pop();
	}
	find_top();
}
}
void push(char a)
{
	stack[top] = a;
	top++;
}
void pop()
{
	if (top == -1)
	{
		printf("0");
		exit(0);
	 //   return 0;	
    }
	else		
		top--;
}
void find_top()
{
	if (top == -1)
		printf("1");
	else
		printf("0");
}
