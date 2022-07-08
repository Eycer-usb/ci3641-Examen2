#include <bits/stdc++.h>
using namespace std;

/*
Esta es el enfoque inicial que se le dio
al problema del tipo recursivo de los numerales
de Church.

En este caso se enfocó como una struct que contiene un apuntador
a una estructura del mismo tipo que representa a su sucesor.

Se Realizaron algunas pruebas sin embargo se descarto 
esta idea. Debido a su similitud con las listas enlazadas
y al hecho que en esta implementacion suc no es una funcion
como indica el enunciado. Sino que se es un apuntador
que manualmente se debe asignar.

Se obtó por implementarlo como una clase
(Vease archivo pregunta_1b.cpp)

*/

struct Church
{
    int value;
    Church *suc;
};


int main(){
    int n;
    cin >> n;
    Church *head = new Church { 0, NULL }, *temp, *i; 
    i = head;
    for (int k = 0; k < n; k++)    
    {
        temp = new Church;
        i->suc = temp;
        temp->value = (i->value) + 1;
        i = temp;
    }

    temp = head;
    while(temp->suc){
        printf("valor: %i, Siguiente: %p\n", temp->value, temp->suc );
        temp = temp->suc;
    }

    printf("%i\n", head->suc->suc->suc->value);


    return 0;
}