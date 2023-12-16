from src.interfaz import interfaz_inicial

def main():    
    try:
        #Ejecutar interfaz inicial
        interfaz_inicial()
    except Exception as e:
        print("Error en la ejecución del programa:" + str(e))
    
if __name__ == "__main__":
    main()