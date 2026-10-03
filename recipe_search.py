import requests

def buscar_recetas(texto):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={texto}"
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        return datos["meals"]
    except requests.exceptions.RequestException:
        print("Error de conexión.")
        return None

def main():
    while True:
        texto = input("Buscar plato o ingrediente: ")
        recetas = buscar_recetas(texto)

        if not recetas:
            print("No se encontraron recetas.")
        else:
            for indice, receta in enumerate(recetas):
                print(f"{indice + 1}. {receta['strMeal']}")
                print("Origin: ", receta["strCountry"])

            receta_elegida = None
            while receta_elegida is None:
                try:
                    eleccion = int(input("Ingresa el número del plato a ver: "))
                    receta_elegida = recetas[eleccion - 1]
                except (ValueError, IndexError):
                    print("El número no se encuentra en la lista, intente de nuevo.")
            
            print(f"Ingredientes para: {receta_elegida['strMeal']}")
            for i in range(1,21):
                ingrediente = receta_elegida[f"strIngredient{i}"]
                medida = receta_elegida[f"strMeasure{i}"]
                if ingrediente:
                    print(f"{medida} {ingrediente}")

            while True:
                respuesta = input("¿Quieres ver las instrucciones? (si/no): ").lower()
                if respuesta == "si":
                    print(receta_elegida["strInstructions"])
                    break
                elif respuesta == "no":
                    break
                else: 
                    print("Debe ingresar 'si' o 'no'.")

        while True:
            seguir = input("¿Buscar otra receta? (si/no): ").lower()
            if seguir == "si" or seguir == "no":
                break
            else:
                print("Debe ingresar 'si' o 'no'.")
        if seguir == "no":
            break
main()
