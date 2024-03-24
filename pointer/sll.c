#include<stdio.h>
#include<stdlib.h>

struct node
{
    char c;
    struct node *link;
};


void print_list(struct node *head) {
    struct node *p;
    p = head;
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
    //Initialize nodes
    struct node *head;
    struct node *one = NULL;
    struct node *two = NULL;
    struct node *three = NULL;

    //Memory Allocation
    one = (struct node *)malloc(sizeof(struct node));
    two = (struct node *)malloc(sizeof(struct node));
    three = (struct node *)malloc(sizeof(struct node));

    //Assigns values
    one->c = 'A';
    two->c = 'B';
    three->c = 'C';

    //Connects node 
    one->link = two;
    two->link = three;
    three->link = NULL;

    //printing node values
    head = one;
    print_list(head);
    printf("\n");

}

//All about singly linked list
