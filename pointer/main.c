#include<stdio.h>

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