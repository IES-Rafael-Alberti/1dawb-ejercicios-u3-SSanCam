"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla."""
def mostrar_lista(asignaturas) -> list:
    asignaturas = ("Matemáticas", "Física", "Química", "Historia", "Lengua")
    return asignaturas

def mostrar_lista(asignaturas) -> list:
    return (print(" - ".join(asignaturas)))
    
def main() -> list:

    asignaturas = ( "Matemáticas", "Física", "Química", "Historia", "Lengua")
    mostrar_lista(asignaturas)
    print()
    
if __name__=="__main__":
    main()