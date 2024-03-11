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

void insertAtBegining(struct node *head) {
    struct node *new = (struct node *)malloc(sizeof(struct node));
    new->link = head;
    head = new; 
}

void insertAtEnd(struct node *head) {
    struct node *new = (struct node *)malloc(sizeof(struct node));
    struct node *t;
    t = head;
    while(t->link != NULL) {
        t = t->link;
    }
    t->link = new;
    new->link = NULL;
}   

int main(void) 
{
    struct node *head;
    struct node *p;
    head = (struct node *)malloc(sizeof(struct node));
}