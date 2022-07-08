/*
Clase que implementa los Numerales de Church
Se define un Valor Contante ZERO y a partir de este
se puede optener cualquier numero natural N como
el sucesor N-esimo de Zero.

La definicion de la clase es recursiva. Al instanciar un
tipo Church y ejecutar el metodo suc() este retorna otro
objeto de tipo Church que representa al sucesor del primero
*/

#include <bits/stdc++.h>
using namespace std;

class Church
{
    public:
    string value = "ZERO";

    /*
    Metodo Sucesor Retorna al Sucesor de 'this' Church
    */
    Church suc() {
        string value = "Suc(" + this->value + ")";
        Church *suc = new Church;
        suc->value = value;
        return *suc;
    }

    /*
    Se define el operador binario + sobre instancias de Church
    y sobre Church + Entero
    Se obtiene la representacion entera del numeral de Church
    para mejorar el rendimiento de la operacion suma sobre 
    objetos de este tipo
    */
    Church operator+( const Church& other ) {
        unsigned int n = this->toInteger();
        unsigned int m = Church::toInteger(other);
        Church result = Church::toChurch(n+m);
        return result;
    }

    Church operator+( const unsigned int& other ) {
        unsigned int n = this->toInteger();
        unsigned int m = other;
        Church result = Church::toChurch(n+m);
        return result;
    }

     /*
    Se define el operador binario * sobre instancias de Church
    Se obtiene la representacion entera de los numerales de Church
    implicados, para mejorar el rendimiento de la operacion producto sobre 
    instancias de este tipo
    */
    Church operator*( const Church& other ) {
        unsigned int n = Church::toInteger(other);
        unsigned int m = Church::toInteger(*this);
        Church result = Church::toChurch(n*m);
        return result;
    }

    /*
    La funcion a continuacion permite Crear un Tipo Church inmediatamente,
    sin la necesidad de obtenerlo recursivamente mediante la 
    aplicacion en secuencia del metodo suc()

    Por ejemplo, en vez de hacer:
    Church tres;
    tres = tres.suc().suc().suc();
    
    Se puede hacer:
    Church tres = Church::toChurch(3);

    Esto evita tener que crear las instancias tres.suc() y tres.suc().suc()
    que solo se utilizan como estructuras de paso;

    Formalmente los Numerales de Church requieren la aplicacion continua
    de la funcion sucesor() K veces para calcular el numeral K-esimo
    sin embargo por terminos de rendimiento computacional
    y teniendo en cuenta el tamaño finito de la memoria de un computador
    se obtó por proporcionar un metodo de generar un tipo Church K evitando
    calcular los K primeros numerales involucrados. Pero esto no es limitante,
    si se desea calcular el numeral K esimo puede hacerse mediante un bucle
    que aplique k veces el metodo suc() a una primera instancia de Church.
    */
    static Church toChurch( unsigned int v ) {
        Church number;
        string funStart = "";
        string funEnd = "";
        while(v--) funStart+="Suc(", funEnd+=")";
        number.value = funStart + number.value + funEnd;
        return number;
    }

    /*
    Cuando es invocado este metodo se retorna el entero al cual
    el numeral representa.
    */
    unsigned int toInteger(){
        unsigned int i = 0;
        for (int j = 0; j < this->value.size(); j++)
        {
            if( this->value[j] == '(' ) i++;
        }

        return i;
    }
    /*
    Permite Calcular el numero natural al cual el
    numeral de Church representa, sin instanciar la clase.
    */
    static unsigned int toInteger( const Church& a ){
        unsigned int i = 0;
        for (int j = a.value.length()-1; j > 0 && a.value[j] != 'O'; j--)
        {
            if( a.value[j] == ')' ) i++;
        }

        return i;
    }
};



int main(){
    unsigned int n, m;
    printf("Introduzca un numero Natural\nn = ");
    cin >> n;
    printf("Introduzca otro numero Natural\nm = ");
    cin >> m;
    Church other = Church::toChurch(m);
    Church number = Church::toChurch(n);
    Church sum = number + other;
    Church product = number * other;
    cout << "n = " << number.value << "\nm = " << other.value <<"\nm+n = " << sum.value <<"\nm*n = " << product.value <<"\n";
    return 0;
}