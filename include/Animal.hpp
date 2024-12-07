#pragma once
#include < Jugador.hpp>
#include <Personaje.hpp>
#include <CircusCharlie.hpp>

class Animal : public Dibujo, public Actualizable,

{
private:
    string nombre;
    int Escenario;
    int Nivel1;

public:
    Animal(/* args */) {}
    ~Animal() {}
};