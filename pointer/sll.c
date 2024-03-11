#include<stdio.h>
#include<stdlib.h>

struct node
{
    char c;
    struct node *link;
};

int main(void) 
{
    struct node *head;
    struct node *p;
    head = (struct node *)malloc(sizeof(struct node));
}