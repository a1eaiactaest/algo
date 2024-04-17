#include <stdio.h>

void display(int *arr, int n){
  for (int i = 0; i < n; i++){
    printf("%d ", arr[i]);
  }
  printf("\n");
}

void swap(int *first, int *second){
  int tmp = *first;
  *first = *second;
  *second = tmp;
}

int part(int *arr, int lower, int upper){
  int i = lower - 1;
  int piv = arr[upper];

  for (int j = lower; j < upper; j++){
    if (arr[j] <= piv){
      i += 1;
      swap(arr+i, arr+j);
    }
  }
  i += 1;
  swap(arr+i, arr+upper);
  return i;
}

void quick_sort(int *arr, int lower, int upper){
  if (upper > lower){
    int piv = part(arr, lower, upper);

    quick_sort(arr, lower, piv-1);
    quick_sort(arr, piv+1, upper);
  }
}

int main(){
  int a[] = {5,9,1,3,4,6,6,3,2};
  int len = sizeof(a)/sizeof(int);
  display(a, len);
  quick_sort(a, 0, len-1);
  display(a, len);
}