#include <stdio.h>
#include <string.h>

void swap(int *first, int *second){
  int tmp = *first;
  *first = *second;
  *second = tmp;
}


void selection_sort(int *arr, int n){
  for (int i=0; i <= n; i++){
    int mini = i;
    for (int j=i+1; j < n; j++){
      if (arr[mini] > arr[j]){
        mini = j;
      }
    }
    if (mini != i){
      // swap pointers
      swap(arr+i, arr+mini);
    }
  }
}

int main(){
  int a[] = {5,9,1,3,4,6,6,3,2};
  int len = sizeof(a)/sizeof(int);
  selection_sort(a, len); 

  for (int i = 0; i <= len-1; i++){
    printf("%d ", a[i]);
  }
  printf("\n");

  return 0;
}