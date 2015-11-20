#include <stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

#define n 4141

float *modelo(float *t, float a, float b, float c, float d);
float likelihood(float *f_obs, float *f_mod);
float *lee_datos(int a);
float dist_norm(float m);

int main(int argc, char **argv){
  int n_steps = atof(argv[1]);
  int n_burn = atof(argv[2]);
  float *f_dat = malloc(n*sizeof(float));
  float *t_dat = malloc(n*sizeof(float));
  float *a_walk = malloc(n_steps*sizeof(float));
  float *b_walk = malloc(n_steps*sizeof(float));
  float *c_walk = malloc(n_steps*sizeof(float));
  float *d_walk = malloc(n_steps*sizeof(float));
  float *l_walk = malloc(n_steps*sizeof(float));
  float *f_init = malloc(n*sizeof(float));
  float *f_prime = malloc(n*sizeof(float));

  f_dat = lee_datos(0);
  t_dat = lee_datos(1);  

  srand(time(NULL));
  a_walk[0] = ((float) rand()/(RAND_MAX));
  b_walk[0] = ((float) rand()/(RAND_MAX));
  c_walk[0] = ((float) rand()/(RAND_MAX));
  d_walk[0] = ((float) rand()/(RAND_MAX));
  
  float l_init=0, l_prime=0;
  float a_prime=0, b_prime=0, c_prime=0, d_prime=0;
  float alpha=0;
  int i;
  for(i=0;i<n_steps;i++){
    
    a_prime = dist_norm(a_walk[i]);
    b_prime = dist_norm(b_walk[i]);
    c_prime = dist_norm(c_walk[i]);
    d_prime = dist_norm(d_walk[i]);

    f_init = modelo(t_dat, a_walk[i], b_walk[i], c_walk[i], d_walk[i]);
    f_prime = modelo(t_dat, a_prime, b_prime, c_prime, d_prime);

    l_init = likelihood(f_dat, f_init);
    l_prime = likelihood(f_dat, f_prime);
    
    alpha = l_prime/l_init;
    
    if(alpha >=1.0){
      a_walk[i+1] = a_prime;
      b_walk[i+1] = b_prime;
      c_walk[i+1] = c_prime;
      d_walk[i+1] = d_prime;
      l_walk[i+1] = l_prime;
    }
    else{
      float beta = ((float) rand()/(RAND_MAX));
      if(beta <= alpha){
	a_walk[i+1] = a_prime;
	b_walk[i+1] = b_prime;
	c_walk[i+1] = c_prime;
	d_walk[i+1] = d_prime;
	l_walk[i+1] = l_prime;
      }
      else{
	a_walk[i+1] = a_walk[i];
	b_walk[i+1] = b_walk[i];
	c_walk[i+1] = c_walk[i];
	d_walk[i+1] = d_walk[i];
	l_walk[i+1] = l_walk[i];
      }
    }
    
  }  
  
  int j;
  for(j=0;j<n;j++){
    printf("%f %f %f %f %f\n",a_walk[i], b_walk[i], c_walk[i], d_walk[i], l_walk[i]);
  }
  return 0;
}

float *modelo(float *t, float a, float b, float c, float d){
  float *f = malloc(n*sizeof(float));
  int i;
  for(i=0;i<n;i++){
    f[i] = a*cos((2.0*M_PI/d)*t[i]+b)+c;
  }
  return f;
}

float likelihood(float *f_obs, float *f_mod){
  float suma = 0;
  int i;
  for(i=0;i<n;i++){
    suma += pow(f_obs[i]-f_mod[i],2);
  }
  //printf("\n\n%f",suma);
  return exp(-(1.0/2.0)*suma);
}

float *lee_datos(int a){
  FILE *entrada;
  if(a == 0){
    entrada = fopen("datos_f.dat","r");
  }
  if(a == 1){
    entrada = fopen("datos_t.dat","r");
  }

  float *x = malloc(n*sizeof(float));
  int i;
  if(entrada == NULL){
    printf("\nERROR AL LEER ARCHIVO\n");
    exit(0);
  }
  for(i=0;i<n;i++){
    fscanf(entrada, "%f ", &x[i]);
  }
  return x;
}

float dist_norm(float m){
  float x = ((float) rand()/(RAND_MAX));
  float rand_norm = (1.0/(0.5*sqrt(2*M_PI)))*exp((1.0/2.0)*pow((x-m)/0.5,2));
  return rand_norm;
}
