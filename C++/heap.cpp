#include<bits/stdc++.h>
using namespace std;

struct Heap{
    int *array;
    int count;
    int capacity;
    int heap_type; 
};

struct Heap *createHeap(int heap_type,int capacity){
    struct Heap *h=(struct Heap *)malloc(sizeof(struct Heap));
    if(h==NULL){
        cout<<"Memory Error"<<endl;
        return;
    }

    h->heap_type=heap_type;
    h->capacity=capacity;
    h->count=0;
    h->array=(int *)malloc(sizeof(int)*h->capacity);
    return h;
}

int parent(struct Heap *h,int i){
    if(i<=0 || i>h->count)
        return -1;
    return (i-1)/2;
}

int left(struct Heap *h,int i){
    int left=2*i+1;
    if(left>h->count)
        return -1;
    return left;
}

int right(struct Heap *h,int i){
    int right=2*i+1;
    if(right>h->count)
        return -1;
    return right;
}

int getMax(struct Heap *h,int i){
    if(h->count==0)
        return -1;
    return h->array[0];
}

void heapify(struct Heap *h,int i){
    int l,r,temp,max;
    l=left(h,i);
    r=right(h,i);
    if(l!=-1 && h->array[l]>h->array[i])
        max=l;
    else max=i;
    if(r!=-1 && h->array[r]>h->array[i])
        max=r;
    if(max!=i){
        temp=h->array[i];
        h->array[i]=h->array[max];
        h->array[max]=temp;
    }
    heapify(h,max);
}

int deleteMax(struct Heap *h){
    int data;
    if(h->count==0)
        return -1;
    data=h->array[0];
    h->array[0]=h->array[h->count-1];
    h->count--;
    heapify(h,0);
    return data;
}

int insert(struct Heap *h,int data){
    if(h->count==h->capacity){
        cout<<"Capacity exceeded"<<endl;
        return -1;
    }
    h->count++;
    int i=h->count-1;
    while(i>=0 && data>h->array[(i-1)/2]){
        h->array[i]=h->array[(i-1)/2];
        i=(i-1)/2;
    }
    h->array[i]=data;
    return data;
}




