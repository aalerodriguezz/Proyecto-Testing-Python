import sys
import os

# Ajuste de ruta para poder importar módulos hermanos o padres
# Esto permite ejecutar el script directamente como 'python charfun.py'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modulo1.funciones import esPalindromo

def main():
    
    print("=======================================================")
    print(" Sistema de comprobación de palíndromos")
    print("=======================================================")
    
    while True:
        try:
            frase = input("\nIntroduce una frase (o escribe 'salir' para terminar): ")
            
            # Condición de salida (case-insensitive)
            if frase.strip().lower() == "salir":
                print("\n[!] Programa finalizado. ¡Hasta luego!")
                break
                
            # Llamada a la lógica
            if esPalindromo(frase):
                print(f"✅ La frase '{frase}' es palíndroma.")
            else:
                print(f"❌ La frase '{frase}' no es palíndroma.")
                
        except KeyboardInterrupt:
            print("\n\n[!] Interrupción detectada. Saliendo...")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
