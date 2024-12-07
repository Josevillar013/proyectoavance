#pragma once
#include < Jugador.hpp>
#include <Personaje.hpp>
#include <CircusCharlie.hpp>
#include <curses.h>

class Jugador
{
private:
    int Edad;
    string nombre;
    int Inicio;
    int Menu;

public:
    Jugador(std::string nombre)
    {
        this->Edad = 0;
        this->Edad = nombre;
        this->
    }
    ~Jugador() {}
    void AsignarNombre
};
