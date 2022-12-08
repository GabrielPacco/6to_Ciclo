#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Persona {
    string dni;
    interface nombre;
    interface codArea;
    interface telf;

    // Getters
    string getNombre() {
        return nombre.getNombre();
    }
    string getDni() {
        return dni;
    }
    string getCodArea(){
        return codArea.getCodArea();
    }
    string getNumTel(){
        return telf.getNumTel();
    }
};

class interface {
    string nombre;
    string codArea;
    string nuTelefono;
public:

    string getNombre(){
        return nombre;
    }
    string getCodArea(){
        return codArea;
    }
    string getNumTel(){
        return nuTelefono;
    }
};


class Empresa {

    string ruc; 
    interface nombre;
    interface codArea;
    interface telf;

    string getRuc() {
        return ruc;
    }
    string getNombre() {
        return nombre.getNombre();
    }
    string getCodArea(){
        return codArea.getCodArea();
    }
    string getNumTel(){
        return telf.getNumTel();
    }
};
