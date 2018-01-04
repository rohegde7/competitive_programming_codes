//https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem
//status: code is correct, 9/15 test cases passed (timeout problem)

/*  I'll be using 2 stacks to implement one queue.
    Structure is the basic user defined data structure.
    Each stack is implemented via Double-Linked-List where 'top' refers to top most element(latest element pushed into stack) and 
        'bottom' refers to 1st element pushed into the stack.
    All the elements are linked via 'tlink' refering to link to the upper element and 
        'blink' refering to link to the lower element in the stack.
    Procedure of dequeuing: 1-Pop all but 1(which needs to be deleted) from the stack1 and push them to stack2
                            2-Pop all from stack2 and push into stack1
*/

#include<stdio.h>
#include<stdlib.h>

//implementing the stacks using structure
struct queue{   //10 <-> 20 <-> 30 <-> 40 <-> 50
    int value;
    struct queue *tlink;
    struct queue *blink;
};

typedef struct queue* Q;

Q top1=NULL, bottom1=NULL, top2=NULL, bottom2=NULL;
    
void enqueue(int val);
void enqueue2(int val);
void dequeue();
void display(Q top, Q bottom);


int main(){
   
    int itr;    //number of iterations
    scanf("%d", &itr);

    int i;
    for(i=0; i<itr; i++){
        int option; //1-enqueue, 2-dequeue, 3-print the head of the queue...
        scanf("%d", &option);

        switch(option){
            case 1:
                {
                    int val;
                    //printf("Enter value: ");
                    scanf("%d", &val);
                    if(top1 == NULL){   //if-else not required...used just for sake of seeing proper funtionality
                        //printf("top1 is null\n");
                        enqueue(val);
                    }
                    else{
                        //printf("top1 is not NULL\n");
                        enqueue(val);
                    }
                    break;
                }

            case 2:
                dequeue();
                break;

            case 3:
                display(top1, bottom1);
                break;

            default:
                printf("Wrong input");
                break;                
        }
    }
    return 0;
}

void enqueue(int val){
    Q temp = (Q)malloc(sizeof(struct queue));
    temp->value = val;
    temp->tlink = NULL;
    temp->blink = NULL;

    if(top1 == NULL){
        top1 = temp;
        bottom1 = temp;
    }
    else{
        top1->tlink = temp;
        temp->blink = top1;
        top1 = temp;
    }
}

void enqueue2(int val){
    Q temp = (Q)malloc(sizeof(struct queue));
    temp->value = val;
    temp->tlink = NULL;
    temp->blink = NULL;

    if(top2 == NULL){
        top2 = temp;
        bottom2 = temp;
    }
    else{
        top2->tlink = temp;
        temp->blink = top2;
        top2 = temp;
    }
}

void dequeue(){
    
    if(top1 == NULL){
        printf("Nothing to del\n");
    }
    else{
        Q temp1 = top1;

        while(temp1->blink != NULL){
            enqueue2(temp1->value); 
            top1 = top1->blink;
            top1->tlink = NULL;
            free(temp1);
            temp1 = top1;
        }
        free(temp1);
        top1 = NULL;
        bottom1 = NULL;

        if(top2 != NULL){
            Q temp2 = top2;
            while(temp2->blink != NULL){
                enqueue(temp2->value);
                top2 = top2->blink;
                top2->tlink = NULL;
                free(temp2);
                temp2 = top2;
            }
            enqueue(temp2->value);
            free(temp2);
            top2 = NULL;
            bottom2 = NULL;
        }
        
        
    }
}

void display(Q top, Q bottom){
    if(top == NULL){
       printf("EMPTY\n");
    }
    else{
        printf("%d\n", bottom1->value);
    }
}