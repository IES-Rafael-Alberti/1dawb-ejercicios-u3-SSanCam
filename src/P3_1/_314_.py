"""Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

limite numeros: 1-49
limite reintegro: 1-9
TAMPOCO PUDEN METERSE NUMEROS REPETIDOS 
"""

def pedir_numeros():
    
    try:
        num_list = 1
        lista_numeros = []
        
        print("Introduce los numeros de tu boleto: ") 
        numero = int(input(f"{num_list}.- "))
        
        while (len(lista_numeros) < 6):
            
            numero = int(input(f"Introduce datos validos\n{num_list}.-  "))
            
            if (numero in range(1,50)) and (numero not in lista_numeros):
                
                lista_numeros.append(numero)
                numero = int(input(f"{num_list}.- "))
                
                num_list += 1
            
            else:
                print("Introduce datos validos.")  
                numero = int(input(f"{num_list}.- "))
  
        
        lista_numeros.sort()
        
        return lista_numeros
    
    except ValueError:
        print("Introduce datos validos.")


    
def pedir_reintegro() -> int:
    
    print("Introduce un numero entre 1-9 como reintegro: ")
    reintegro = int(input())
    
    return reintegro
    

def main():
    
    try:

        lista_numeros = pedir_numeros()
        reintegro = pedir_reintegro()
        
        resultado = f"Tus numeros de boleto ordenados son: {lista_numeros} -R: {reintegro}"
        
        return print(resultado)
    
    except ValueError :
        print("Error.")  
    
    
if __name__=="__main__":
    main()