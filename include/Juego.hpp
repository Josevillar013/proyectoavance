#pragma once
#include <Vector.hpp>
#include <Dibujo.hpp>
#include <Actualizable.hpp>

class Juego : public Dibujo, public Actualizable
{
private:
    // Vector posicion;

public:
    Juego() : Dibujo("Payaso")
    {
        this->posicion = Vector();
    }
    Payaso(int x, int y) : Dibujo("cow")
    {
        // this->posicion.DesplazarX(x);
        // this->posicion.DesplazarY(y);
    }
    void Actualizar()
    {
        this->posicion.DesplazarX(1);
        // this->posicion.CambiarDireccionX();
    }
    void Avanzar()
    {
        this->posicion.DesplazarX(1);
    }
    void CambiarDireccion()
    {
        this->posicion.CambiarDireccionX();
    }
    Vector LeerPosicion()
    {
        return this->posicion;
    }

    ~Juego()
    {
    }