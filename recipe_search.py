import requests

def buscar_recetas(texto):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={texto}"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos["meals"]

def main():
    texto = input("Buscar plato o ingrediente: ")
    recetas = buscar_recetas(texto)

    try:
        for receta in (recetas):
            print(receta["strMeal"])
            print("Origin: ", receta["strCountry"])
    except TypeError:
        print("No se encontraron recetas.")
main()
