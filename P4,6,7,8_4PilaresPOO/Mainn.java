// Clase base "Animal"
class Animal {
    String nombre;

    public Animal(String nombre) {
        this.nombre = nombre;
    }

    public void hablar() {
        System.out.println("El animal hace un sonido.");
    }
}

// Clase derivada "Perro" que hereda de "Animal"
class Perro extends Animal {
    String raza;

    public Perro(String nombre, String raza) {
        // Llama al constructor de la clase base para inicializar el atributo "nombre"
        super(nombre);
        this.raza = raza;
    }

    // Sobrescribe el método "hablar" de la clase base
    @Override
    public void hablar() {
        System.out.println("Guau guau");
    }

    public void ladrar() {
        System.out.println("El perro está ladrando.");
    }
}

public class Mainn {
    public static void main(String[] args) {
        // Crear objetos de las clases
        Animal animal = new Animal("Desconocido");
        Perro perro = new Perro("Max", "Labrador");

        // Llamar a los métodos de los objetos
        animal.hablar(); // Imprime: "El animal hace un sonido."
        perro.hablar(); // Imprime: "Guau guau" (método sobrescrito)
        perro.ladrar(); // Imprime: "El perro está ladrando." (método propio)

        // Acceder a los atributos de los objetos
        System.out.println(animal.nombre); // Imprime: "Desconocido"
        System.out.println(perro.nombre); // Imprime: "Max" (atributo heredado)
        System.out.println(perro.raza); // Imprime: "Labrador" (atributo propio)
    }
}