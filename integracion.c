#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define N 1000000

void nAleatorios(double *nums);
double func(double x);

int main() {

  FILE *fout;
  fout = fopen("resultados.txt", "w+");

  srand48(time(NULL));

  double *nums =(double *) malloc(N*sizeof(double));
  double *x =(double *) malloc(N*sizeof(double));

  double dx = 0;
  dx = 1.0/N;
  x[0] = 0.0;

  nAleatorios(nums);

  int i;
  int cuenta = 0;
  if (nums[0] < func(x[0])) {
    cuenta += 1;
  }
  for ( i = 1; i < N; i++) {
    x[i] = x[i-1] + dx;
    if (nums[i] < func(x[i])) {
      cuenta += 1;
    }
  }

  double integral = 0;
  integral = (double) cuenta/N;
  fprintf(fout,"El valor de la integral es : %lf\n", integral);
  fclose(fout);

  return 0;
}

double func(double x){
  return exp(-1.0*x);
}

void nAleatorios(double *nums){
  int i;
  for ( i = 0; i < N; i++) {
    nums[i] = drand48();
  }
}
