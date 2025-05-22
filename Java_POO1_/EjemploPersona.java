class Persona {
    // Atributos
    String nombre;
    int edad;
    // Constructor
    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
    // Método sin parámetros
    public void mostrarInformacion() {
        System.out.println("Nombre: " + nombre + ", Edad: " + edad);
    }
    // Método con parámetros
    public void actualizarEdad(int nuevaEdad) {
        this.edad = nuevaEdad;
    }
}


public class EjemploPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Carlos", 28); // Crear objeto
        persona1.mostrarInformacion(); // Llamar método
        persona1.actualizarEdad(30); // Actualizar edad
        persona1.mostrarInformacion();
    }
}
