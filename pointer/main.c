#include<stdio.h>
#include<stdlib.h>
struct node
{
    /* data */
    int i;
    int *c;
};

int main() {
    struct node a[2], *p;
    int b[2] = {30, 40};
    p = &a[0];
    a[0].i = 10;
    a[1].i = 20;
    a[0].c = b;
    /* find 
    ++p->i;
    x = (++p)->i;
    x = (p++)->i;
    x = *p->i;
    x = *p->c++;
    x = (*p->c)++;
    x = *p++->c;
    */
}

/* There are three types of storage class -> Static, extern, register
    register -> Store in the register, dont store variable in the register u can store address of a variacle in the register.
*/



struct node
{
    /* data */
    int i;
    struct node *l;
};

struct node *p;
p = (struct node *)malloc(sizeof(struct node));
