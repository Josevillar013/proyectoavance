#pragma once

class Vector
{
private:
    int x;
    int y;
    int direccion_x;
    int direccion_y;

public:
    // Default constructor
    Vector()
    {
        this->x = 0;
        this->y = 0;
        this->direccion_x = 1;
        this->direccion_y = 1;
    }

    // Parameterized constructor
    Vector(int x, int y)
    {
        this->x = x;
        this->y = y;
        this->direccion_x = 1;
        this->direccion_y = 1;
    }

    // Function to change direction along the x-axis
    void CambiarDireccionX()
    {
        this->direccion_x *= -1;
    }

    // Function to change direction along the y-axis
    void CambiarDireccionY()
    {
        this->direccion_y *= -1;
    }

    // Function to displace along the x-axis
    void DesplazarX(unsigned int x)
    {
        this->x += x * this->direccion_x;
    }
        void DesplazarY(unsigned int y)
    {
        this->x += y;
    }

    // Function to read the x-coordinate
    int LeerX()
    {
        return this->x;
    }
    int LeerY()
    {
        return this->y;
    }
    // Destructor
    ~Vector()
    {
        // Destructor implementation if needed
    }
};