#include <stdio.h>
#include <string.h>
#include <unistd.h>

void imprime_gym(int gimnasio[10]){
printf("\n");
  for(int i =0 ;i <10 ; i ++ ){
    printf("[%d]",gimnasio[i]);
  }
}


int main(){

  struct Pokemon{
    int id;
    char nombre[50];
    char grito[50];
    int tipo;
    float fuerza;
    float defensa;
    int genero;
    int movimiento;
    int rango;
  };

  struct Pokemon mascota[2];

  strcpy(mascota[0].nombre,"pikachu");
  strcpy(mascota[0].grito,"pika pika");
  mascota[0].id = 2;
  mascota[0].tipo = 1;
  mascota[0].fuerza = 10;
  mascota[0].defensa= 5;
  mascota[0].genero = 1;
  mascota[0].movimiento = 2;
  mascota[0].rango = 3;

  strcpy(mascota[1].nombre,"Charmander");
  strcpy(mascota[1].grito,"char char");
  mascota[1].id = 7;
  mascota[1].tipo = 3;
  mascota[1].fuerza = 12;
  mascota[1].defensa= 7;
  mascota[1].genero = 0;
  mascota[1].movimiento = 1;
  mascota[1].rango = 2;

  int gimnasio[10]={0,0,0,0,0,0,0,0,0,0};
//inicializa el juego
  gimnasio[0] = mascota[0].id;
  gimnasio[9] = mascota[1].id;
  
  imprime_gym(gimnasio);
int j=0,p=9;
  for (;1;){
sleep(5);
    //if(gimnasio[j+2] == p || gimnasio[j+1] == p){
    for(;1;j=j+2){
      gimnasio[j] = 0;
      gimnasio[j+2] = mascota[0].id;
      break;
    }
    for(;1;p=p-1){
      gimnasio[p] = 0;
      gimnasio[p-1] = mascota[1].id;
      break;
    }
    imprime_gym(gimnasio);
}
///caminar
  
//  printf("%s\n",humano.nombre);
//  printf("%d \n",humano.edad);
  return 0;
}
