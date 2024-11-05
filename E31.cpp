// Name - Pranalee Raut
// Class - SE-2
// PRN - F23112036
// Batch - Q
// Seat N0 - F190320536

// Group E-31
// Title - A double-ended queue(deque) is a linear list in which additions and deletions may be made at either end. Obtain a data 
// representation mapping a deque into a one-dimensional array. Write C++ program to simulate deque with functions to add and delete 
// the elements from either end of the deque.

#include<iostream>
using namespace std;

class deque1
{
public:
    int f,r,data[100],n;
    deque1()
    {
        f =  r = -1;
        cout<<"Enter number of elements: ";
        cin>>n;
    }
    void enqueuef();
    void enqueuer();
    void dequeuef();
    void dequeuer();
    bool isEmpty();
    bool isFull();
    void display();
};

void deque1::enqueuef()
{
    int id;
    cout<<"\nEnter element: ";
    cin>>id;
    if(!isFull())
    {
        if(f == -1)
            f = r = 0;
        else if(f == 0)
            f = n - 1;
        else
            f--;
        data[f] = id;
    }
    else
        cout<<"\nQueue is full....\n";
}

void deque1::enqueuer()
{
    int id;
    cout<<"\nEnter element: ";
    cin>>id;
    if(!isFull())
    {
        if(f == -1)
            f = r = 0;
        else if(r == n - 1)
            r = 0;
        else
            r++;
        data[r] = id;
    }
    else
        cout<<"\nQueue is full....\n";
}

void deque1::dequeuef()
{
    if(!isEmpty())
    {
        if(f == r)
            f = r = -1;
        else if(f == n-1)
            f = 0;
        else
            f++;
    }
    else
        cout<<"\nQueue is empty....\n";
}

void deque1::dequeuer()
{
    if(!isEmpty())
    {
        if(f == r)
            f = r = -1;
        else if(r == 0)
            r = n-1;
        else
            r--;
    }
    else
        cout<<"\nQueue is empty....\n";
}

void deque1::display()
{
    int i;
    cout<<"\nDeque: ";
    if(!isEmpty())
    {
        i = f;
        do
        {
            cout<<data[i]<<" ";
            i = (i+1)%n;
        }while(i != (r+1)%n);
    }
    else
        cout<<"\nQueue is empty....\n";
    cout<<"\n";
}

bool deque1::isFull()
{
    if((f==0 && r >= n - 1)|| f==r+1)
        return true;
    else
        return false;
}

bool deque1::isEmpty()
{
    if(r == -1)
        return true;
    else
        return false;
}

int main()
{
    deque1 obj;
    int ch;
    bool flag = true;
    while(flag)
    {
        cout<<"\n****YOUR CHOICES ARE****\n";
        cout<<"\n1. Enqueue(at front) \n2. Enqueue(at rear) \n3. Dequeue(at front) \n4. Dequeue(at rear) \n5. Display queue \n6. Exit";
        cout<<"\nEnter your choice: ";
        cin>>ch;
        switch(ch)
        {
        case 1:
            obj.enqueuef();
            obj.display();
            break;

        case 2:
            obj.enqueuer();
            obj.display();
            break;

        case 3:
            obj.dequeuef();
            obj.display();
            break;

        case 4:
            obj.dequeuer();
            obj.display();
            break;

        case 5:
            obj.display();
            break;

        case 6:
            flag = false;
            break;

        default:
            cout<<"\nEnter valid choice!!!\n";
            break;
        }
    }
    return 0;
}

// Output - 
// Enter number of elements: 5

// ****YOUR CHOICES ARE****

// 1. Enqueue(at front)
// 2. Enqueue(at rear)
// 3. Dequeue(at front)
// 4. Dequeue(at rear)
// 5. Display queue
// 6. Exit
// Enter your choice: 1

// Enter element: 2

// Deque: 2

// ****YOUR CHOICES ARE****

// 1. Enqueue(at front)
// 2. Enqueue(at rear)
// 3. Dequeue(at front)
// 4. Dequeue(at rear)
// 5. Display queue
// 6. Exit
// Enter your choice: 2

// Enter element: 3

// Deque: 2 3

// ****YOUR CHOICES ARE****

// 1. Enqueue(at front)
// 2. Enqueue(at rear)
// 3. Dequeue(at front)
// 4. Dequeue(at rear)
// 5. Display queue
// 6. Exit
// Enter your choice: 2

// Enter element: 4

// Deque: 2 3 4

// ****YOUR CHOICES ARE****

// 1. Enqueue(at front)
// 2. Enqueue(at rear)
// 3. Dequeue(at front)
// 4. Dequeue(at rear)
// 5. Display queue
// 6. Exit
// Enter your choice: 2

// Enter element: 6

// Deque: 2 3 4 6

// ****YOUR CHOICES ARE****

// 1. Enqueue(at front)
// 2. Enqueue(at rear)
// 3. Dequeue(at front)
// 4. Dequeue(at rear)
// 5. Display queue
// 6. Exit
// Enter your choice: 2

// Enter element: 10

// Deque: 2 3 4 6 10

// ****YOUR CHOICES ARE****

// 1. Enqueue(at front)
// 2. Enqueue(at rear)
// 3. Dequeue(at front)
// 4. Dequeue(at rear)
// 5. Display queue
// 6. Exit
// Enter your choice: 3

// Deque: 3 4 6 10

// ****YOUR CHOICES ARE****

// 1. Enqueue(at front)
// 2. Enqueue(at rear)
// 3. Dequeue(at front)
// 4. Dequeue(at rear)
// 5. Display queue
// 6. Exit
// Enter your choice: 4

// Deque: 3 4 6

// ****YOUR CHOICES ARE****

// 1. Enqueue(at front)
// 2. Enqueue(at rear)
// 3. Dequeue(at front)
// 4. Dequeue(at rear)
// 5. Display queue
// 6. Exit
// Enter your choice: 5

// Deque: 3 4 6

// ****YOUR CHOICES ARE****

// 1. Enqueue(at front)
// 2. Enqueue(at rear)
// 3. Dequeue(at front)
// 4. Dequeue(at rear)
// 5. Display queue
// 6. Exit
// Enter your choice: 6