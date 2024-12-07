#include <Ventana.hpp>
#include <Juego.hpp>
#include <list>
#include <iostream>
#include<Leon.hpp>
using namespace std;

int main(int argc, char const *argv[])
{
    CircusCharlie* vaca1= new CircusCharlie();
    CircusCharlie* vaca2= new CircusCharlie(30,0);
    CircusCharlie* vaca3= new CircusCharlie(50,10);

    Ventana* ventana= new Ventana();

    list<Dibujo*> dibujos;
    dibujos.push_back(payaso1);
    dibujos.push_back(payaso2);
    dibujos.push_back(payaso3);

    list<Actualizable*> actualizables;
    actualizables.push_back(vaca1);

    while (!ventana->DeboCerrar())
    {
        int key = getch();
        if(key=='a'||key==KEY_LEFT)
        {
            vaca1->Avanzar();
        }
        if(key=='d'||key==KEY_RIGHT)
        {
            vaca1->CambiarDireccion();
        }
        if(key==' ')
        {
            Proyectil* p = new Proyectil(payaso1->LeerPosicion());
            dibujos.push_back(p);
            actualizables.push_back(p);
        }
        ventana->Dibujar(dibujos);
        ventana->Actualizar(actualizables);
    }

    return 0;
}