#pragma once
#include <curses.h>
#include <unistd.h>
#include <Dibujo.hpp>
#include <Actualizable.hpp>
#include <list>
class Ventana
{
private:
    int x;
    int y;
    bool cerrar;

public:
    Ventana()
    {
        // iniciar pantalla
        initscr();
        // eliminar cursor pantalla
        noecho();
        curs_set(FALSE);

        // no bloquear consola
        nocbreak();

        getmaxyx(stdscr, y, x);
        cerrar = false;
    }

    void Actualizar(list<Actualizable *> listaActualizables)
    {
        // getch()
        for (auto &&iterador : listaActualizables)
        {
            iterador->Actualizar();
        }

        // a.Actualizar();
        usleep(41000); // micro segundos en los que dibuja
    }

    void Dibujar(list<Dibujo *> listaDibujo)
    {
        clear();
        // d.Dibujar();
        box(stdscr, '|', '-');
        for (auto &&dibujo : listaDibujo)
        {
            dibujo->Dibujar();
        }

        refresh();
    }
    bool DeboCerrar()
    {
        return this->cerrar;
    }

    void Cerrar()
    {
        this->cerrar = true;
    }

    ~Ventana()
    {
        endwin();
    }
};