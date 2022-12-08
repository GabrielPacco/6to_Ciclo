#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Persona {
    string nombre;
    string dni;
    telefono telf;
    // Getters
    string getNombre() {
        return nombre;
    }
    string getDni() {
        return dni;
    }
    string getTelefono() {
        return telf.getNumeroTelefono();
    }
};

class telefono {

    string codArea;
    string nuTelefono;
public:

    string getNumeroTelefono() {
        return nuTelefono + codArea;
    }
};

class Empresa {

    string nombre;
    string ruc;
    telefono telf;

    // Getters
    string getNombre() {
        return nombre;
    }
    string getRuc() {
        return ruc;
    }
    string getTelefono() {
        return telf.getNumeroTelefono();
    }

};
