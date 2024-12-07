#pragma once
#include <Dibujo.hpp>
#include <Actualizable.hpp>
#include <list>

class Pelota : public Dibujo, public Actualizable
{
private:
    int numeroSaltos;

public:
    Pelota(/* args */) : Dibujo("Pelota") {}
    ~Pelota() void Actualizar()
    {
    }
};