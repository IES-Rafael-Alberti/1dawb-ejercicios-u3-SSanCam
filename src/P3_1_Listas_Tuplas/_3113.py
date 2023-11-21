"""Escribir un programa que pregunte por una muestra de números, separados por comas, 
los guarde en una lista y muestre por pantalla su media y desviación típica."""
import os 
def clear_terminal():
    os.system('cls')

def pedir_numeros() -> list:
    
 
    try:
        
        indice = 1
        numeros = []
        seguir = True
        
        print('Introduce numeros: ')

        while (seguir == True):
                                
            try:     
                    
                numero = int(input(f'Numero {indice} -> '))
                
                numeros.append(numero)
                
                print('Quieres seguir? si / no')
                seguir = input()
                if (seguir.lower() == 'si'):
                    seguir = True 
                    
                elif (seguir.lower() == 'no'): 
                    seguir = False
                
                else:
                    raise ValueError ('Datos no validos. Introduce \'si\'o \'no\' ')
                
                indice += 1
                            
            except ValueError as ve:
                print (f'ERROR\n{ve}')
                return []
        
        return numeros
        
    except (Exception):
        
        return []
    

def media_numeros(lista_numeros: list) -> int:
    if (not lista_numeros):
        return 0.0
    media = sum(lista_numeros) // len(lista_numeros)

    return media 


def main():
    
    clear_terminal()
    
    lista_numeros = pedir_numeros()
    
    media = media_numeros(lista_numeros)
    
    resultado = print(f'De tu lista de numeros: {lista_numeros} \nLa media es de: {media}')
    
    
    return resultado

if __name__=="__main__":
    main()