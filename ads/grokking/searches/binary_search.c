#include <stdio.h>

int binary_search(int nums[], int n, int v){
  /**
   * @brief Search for @param item in @param nums using binary search algorithm.
   * @return -1 if @param item not found, else index.
   */
  int low = 0;
  int high = n - 1;

  while (low <= high){
    int mid = low + high;
    int guess = nums[mid];

    if (guess == v){
      return mid;
    }
    if (guess > v){
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return -1;
}

void fill(int *arr, int size){
  /**
   * @brief Generate a sequence of numbers in range of N.
   */

  for (int i=0; i<=size; i++){
    arr[i] = i;
  }
}

int main(int argc, char *argv[]){
  int a[100];
  int n = sizeof(a)/sizeof(int);

  fill(a, n);

  for (int i=0; i<=n; i++){
    printf("%d, ", a[i]);
  }
  printf("\n");

  int res = binary_search(a, n, 101);
  printf("%d\n", res);
  return 0;
}