#include<stdio.h> 
 
/* 
    Un programa que recorre una matriz de 5x5. 
    La matriz contiene rutas 
    Determinar cual es la ruta mas barata 
     
    !! - IMPORTANTE - !! 
     
    1. Leer la matriz (recorrido) 
    2. Comparar elementos de la matriz(para saber cual ruta es mas barata) 
    3. Imrprimir la ruta mas barata. 
 
*/ 
 
/* 
    La matriz esta constituida por: 
     
    Columnas: (x) un total de 5 columnas 
    Filas: (h) un total de 5 Filass 
     
    - Determinar el elemento de valor mas alto 
    - Determinar el elemento de menor valor 
*/ 
 
 
 
int main() 
{ 
    int h, x; 
    int rout, rout2; 
    int matriz[5][5] = {
    Y      0    1   2   3   4  
    X   0 {25, 40, 06, 11, 21}, 
        1 {02, 08, 15, 12, 29}, 
        2 {32, 07, 36, 37, 35}, 
        3 {23, 57, 05, 40, 31}, 
        4 {22, 14, 10, 17, 48}
    }; 

    inicio -> 0,0
    final  -> 3,3
    /*
     X,Y
    [0,0] -> [0,1],[1,0]
    [0,1] -> [0,0][0,2][1,1] 
    [1,0] -> [0,0][1,1][0,2]
    [1,1] -> [0,1][1,0][2,1][1,2]

     6 -> 5,1,7,11




    */


    // asignamos "por default" la posicion 0 a la variable rout 
    rout = matriz[0][0]; 
    rout2 = rout; 
    /* 
        Esto es para comparar los numeros que estan dentro de nuestra matriz 
        asi sabremos cual elemento tiene menor valor, que por consecuencia, sera la mejor ruta en este caso 
    */ 
    for(x = 0; x < 5; x++) 
    { 
        for(h = 0; h < 5; h++) 
        { 
            printf("Ruta: [%d]\n",matriz[x][h]); 
             
            // si el elemento de la posicion 1 es mayor a la posicion inicial, entonces rout toma el elemento de la posicion 1 
            if(matriz[x][h] > rout) 
            { 
                rout = matriz[x][h]; 
            } 
            if(matriz[x][h] < rout2) 
            { 
                rout2 = matriz[x][h]; 
            } 
        } 
    } 
    printf("\n"); 
    printf("\nLa ruta mas costosa es: %d", rout); 
    printf("\nLa mejor ruta es: %d", rout2); 
    return 0; 
}