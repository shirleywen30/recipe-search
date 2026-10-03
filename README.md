# Buscador de Recetas

Script en Python que consume la API pública de [TheMealDB](https://www.themealdb.com/api.php) para buscar recetas por nombre o ingrediente, mostrar sus ingredientes y, opcionalmente, el paso a paso para prepararlas.

## Qué hace

1. Pide un plato o ingrediente a buscar
2. Muestra la lista de recetas encontradas, con su país de origen
3. Permite elegir una receta de la lista
4. Muestra los ingredientes y medidas de esa receta
5. Pregunta si quieres ver las instrucciones paso a paso
6. Permite buscar otra receta sin cerrar el programa

## Tecnologías

- Python 3
- [requests](https://pypi.org/project/requests/) para consumir la API

## Cómo correrlo

1. Clona el repositorio
2. Instala las dependencias: pip install -r requirements.txt
3. Corre el script: python recipe_search.py

## Qué aprendí / practiqué

- Consumir una API REST con GET
- Procesar respuestas JSON
- Manejo de errores (datos no encontrados, entrada inválida del usuario, fallas de conexión)
- Loops de interacción con el usuario (`while True` con validación)