/*************************************************
* Author: Guyon Pince van der Aa
* Description: Asks the user what operation
*    should be preformed, then asks for 2 numbers
*   and preform the selected operation.
* Date: 17-5-2018
************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define ADD 43
#define SUBTRACT 45
#define MULTIPLY 42
#define DEVIDE 47
#define MOD 37
#define OPTIONS 5
#define EXIT 48
const int opperants[] = {ADD, SUBTRACT, MULTIPLY, DEVIDE, MOD, EXIT};


// UI functions
void print_menu();
int operation_choice();
void number_input(float *first, float *second);

// Operation functions
float addNums(float first, float second);
float subtractNums(float first, float second);
float multiplyNums(float first, float second);
float divideNums(float first, float second);
int modulusNums(float first, float second);
bool opperantValid(int op);

/*************************************************
* Function name: int main(void)
* Parameters: none
* Return type: int(system 0)
* Description: Asks the user what operation
*    should be preformed, then asks for 2 numbers
*   and preform the selected operation.
*************************************************/
int main()
{
    float argA, argB;
    int selection, again;
    int sel;

    do
    {
        system("cls");
        printf("selection = %d\n", (int)'-');
        print_menu();
        sel = operation_choice();
        if(opperantValid(sel))
            number_input(&argA, &argB);
        
        switch(sel)
        {
            case EXIT:
                return 0;
                break;
            case ADD:
                printf("Answer = %f\n\n" ,addNums(argA, argB));
                break;
            case SUBTRACT:
                printf("Answer = %f\n\n" ,subtractNums(argA, argB));
                break;
            case MULTIPLY:
                printf("Answer = %f\n\n" ,multiplyNums(argA, argB));
                break;
            case DEVIDE:
                if(argB != 0)
                    printf("Answer = %f\n\n" ,divideNums(argA, argB));
                else
                    printf("ERROR: Divide by 0\n\n");
                break;
            case MOD:
                if(argB != 0)
                    printf("Answer = %d\n\n" ,modulusNums(argA, argB));
                else
                    printf("ERROR: X %% 0 is invalid\n\n");
                break;
            default:
                printf("Invalid selection");
        }
        printf("Enter something to run again ");
        scanf("%d", &again);
    }while(sel != 0);
}

/*************************************************
* Function name: void print_menu()
* Parameters: none
* Return type: void
* Description: prints the menu
*************************************************/
void print_menu()
{
    printf("MENU\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n0. Exit\n\n");
    return;
}

/**************************************************
* Function name: int operation_choice(int *pSelect)
* Parameters: int *pSelect
* Return type: int
* Description: Asks the user for their selection
*   from the menu
**************************************************/
int operation_choice()
{
    char input;
    
    printf("Enter your choice: ");
    scanf(" %c", &input);
    // pSelect = (int)input;
    int s = (int)input;
    printf("\n");
    return s;
}

/**************************************************************
* Function name: void number_input(float *first, float *second)
* Parameters: int *first, int *second
* Return type: void
* Description: Asks the user for two numbers
**************************************************************/
void number_input(float *first, float *second)
{

    printf("First number\t= ");
    scanf("%f", first);
    printf("Second number\t= ");
    scanf("%f", second);
}

/**************************************************************
* Function name: float addNums(float first, float second)
* Parameters: int *first, int *second
* Return type: float
* Description: Adds two numbers
**************************************************************/
float addNums(float first, float second)
{
    float ans;
    ans = first + second;
    return ans;
}

/**************************************************************
* Function name: float subtractNums(float first, float second)
* Parameters: int *first, int *second
* Return type: float
* Description: Subtracts two numbers
**************************************************************/
float subtractNums(float first, float second)
{
    float ans;
    ans = first - second;
    return ans;
}

/**************************************************************
* Function name: float multiplyNums(float first, float second)
* Parameters: int *first, int *second
* Return type: float
* Description: Multiplies two numbers
**************************************************************/
float multiplyNums(float first, float second)
{
    float ans;
    ans = first * second;
    return ans;
}

/**************************************************************
* Function name: float divideNums(float first, float second)
* Parameters: int *first, int *second
* Return type: float
* Description: Divides two numbers
**************************************************************/
float divideNums(float first, float second)
{
    float ans;
    ans = first / second;
    return ans;
}

/**************************************************************
* Function name: int modulusNums(float first, float second)
* Parameters: int *first, int *second
* Return type: int
* Description: Takes the modulus of two numbers
**************************************************************/
int modulusNums(float first, float second)
{
    int ans;
    ans =  (float)(((int)first % (int)second));
    return ans;
}

bool opperantValid(int op)
{
    for (int i = 0; i < OPTIONS; i++)
    {
        if (opperants[i] == op)
        { 
            return true;
        }
    }
    return false;
}