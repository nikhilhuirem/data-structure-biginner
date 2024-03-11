#include<stdio.h>
#include<stdlib.h>

struct node
{
    char c;
    struct node *link;
};


void print_list(struct node *head) {
    struct node *p;
    p = head->link;
    while(p != NULL) {
        printf("%c", p->c);
        p = p->link;
    }
}

int main(void) 
{
    struct node *head;
    struct node *p;
    head = (struct node *)malloc(sizeof(struct node));
}