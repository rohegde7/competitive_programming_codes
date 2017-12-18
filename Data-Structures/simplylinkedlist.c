//status: DONE :)

#include<stdio.h>
#include<stdlib.h>

struct node{
    int value;
    struct node *link;
};

typedef struct node* NODE;

void add_node(int value);
void delete_node_tail();
void delete_node_head();
void display_node();

NODE head = NULL;
NODE tail = NULL;

int main(){

    int choice; //user's choice on what operation he wants to do on the linked list

    printf("Welcome to a simple linked list\n");

    printf("Enter your choice:\n");

    while(1){
        printf(" 1-Insert\n 2-Delete Head\n 3-Delete Tail\n 4-Display the entire node\n 5-Exit\n");
        scanf("%d", &choice);

        switch(choice){
            case 1:
                printf("Enter a value for your new node: ");
                int val;
                scanf("%d", &val);
                add_node(val);
                break;

            case 2:
                delete_node_head();
                break;

            case 3:
                delete_node_tail();
                break;

            case 4:
                display_node();
                break;

            case 5:
                return;

            default:
                printf("Wrong input\n");
                break;
        }
    }

    return 0;
}

void add_node(int value){
    NODE temp;
    temp = (NODE)malloc(sizeof(NODE));
    temp->value = value;
    temp->link = NULL;

    if(tail == NULL){
        head = temp;
        tail = temp;
    }
    else{
        tail->link = temp;
        tail = temp;
    }
}

void delete_node_head(){
    if(head == NULL){
        printf("Nothing to delete\n");
    }
    else{
        NODE temp;
        temp = head;
        head = head->link;
        free(temp);
    }

    display_node();
}

void delete_node_tail(){
    if(head == NULL){
        printf("Nothing to delete\n");
    }
    else{
        NODE temp;
        temp = head;

        while(temp->link != tail){
            temp = temp->link;
        }
        temp->link = NULL;

        free(tail);
        tail = temp;
    }

    display_node();
}

void display_node(){
    if(head == NULL){
        printf("No nodes present.\n");
    }
    else{
        NODE temp = head;

        while(temp->link != NULL){
            printf("%d\t", temp->value);
            temp = temp->link;
        }

        sprintf("%d\n", temp->value);
    }
}
