#include <iostream>     
#include <cassert>  

using namespace std;

/*
Clase que implementa un arbol binario
y permite verificar si dicho arbol es 
max-heap y si es un max-heap simetrico

*/

class BinaryTree
{

public:
    int value;
    BinaryTree *leftTree = NULL;
    BinaryTree *rightTree = NULL;
    BinaryTree(int leaf);
    BinaryTree(int leaf, BinaryTree *left, BinaryTree *right);
    string posOrderPath();
    string preOrderPath();
    bool isMaxHeap();
    bool isSimetricMaxHeap();
};

/*
Constructor para Hoja del arbol
*/
BinaryTree::BinaryTree(int leaf)
{
    value = leaf;
}

/*
Constructor para arbol con ramas
*/
BinaryTree::BinaryTree(int leaf, BinaryTree *left, BinaryTree *right)
{
    value = leaf;
    leftTree = left;
    rightTree = right;
}

/*
Se retorna un string con
la secuencia de los nodos en pos-orden
el orden es ramaIzquierda,ramaDerecha,Raiz
*/
string BinaryTree::posOrderPath()
{
    string ans = "";
    // Left Sub tree 
    if( this->leftTree ){
        ans += this->leftTree->posOrderPath();
    }
    // Right Sub Tree
    if( this->rightTree ){
        ans += this->rightTree->posOrderPath();
    }
    // Root
    ans += to_string(this->value) + ",";
    return ans;
}

/*
Se retorna un string con
la secuencia de los nodos en pre-orden
el orden es Raiz,ramaIzquierda,ramaDerecha,
*/
string BinaryTree::preOrderPath()
{
    //Root
    string ans = to_string(this->value) + ",";
    // Left Sub tree 
    if( this->leftTree ){
        ans += this->leftTree->preOrderPath();
    }
    // Right Sub Tree
    if( this->rightTree ){
        ans += this->rightTree->preOrderPath();
    }
    return ans;
}

/*
Se Verifica si el arbol binario es un Max-Heap
*/
bool BinaryTree::isMaxHeap()
{
    bool ans = true;
    if(this->leftTree)
    {
        ans = (ans && this->leftTree->isMaxHeap() &&
               this->leftTree->value <= this->value );
    }
    if(this->rightTree)
    {
        (ans && this->rightTree->isMaxHeap() &&
               this->rightTree->value <= this->value );
    }
    return ans;    
}

/*
Se verifica si una instancia de BinaryTree cumple la
propiedad de ser un max-heap simetrico

Se considera que un maxheap es simetrico si y solo si
los recorridos en pre-orden y pos-orden del arbol
producen la misma secuencia

*/
bool BinaryTree::isSimetricMaxHeap()
{
    string preOrder = this->preOrderPath();
    string posOrder = this->posOrderPath();
    return preOrder == posOrder and this->isMaxHeap();
}




//////////////////////////////////////////////////////


/*
Se presenta a continuacion un conjunto de puebas
de la clase definida mas arriba
*/
int main()
{
    //Inicializacion
    BinaryTree pleaseDont = BinaryTree(50);
    assert(pleaseDont.value == 50);
    //Filling Tree
    BinaryTree leftBranch = BinaryTree(20);
    BinaryTree rightBranch = BinaryTree(20);
    BinaryTree* leftPtr = &leftBranch;
    BinaryTree* rightPtr = &rightBranch;
    BinaryTree tree = BinaryTree(20, leftPtr, rightPtr);
    BinaryTree a = BinaryTree(20),b = BinaryTree(20), c = BinaryTree(20), d = BinaryTree(20);
    leftBranch.leftTree = &a;
    leftBranch.rightTree = &b;
    rightBranch.leftTree = &c;
    rightBranch.rightTree = &d;
    // PreOrder travel
    cout << tree.preOrderPath() << endl;
    // PosOrder travel
    cout << tree.posOrderPath() << endl;
    // Is Maxheap?
    cout << tree.isMaxHeap() << endl;
    // Is Simetric a maxHeap?
    cout << tree.isSimetricMaxHeap() << endl;

    return 0;
}