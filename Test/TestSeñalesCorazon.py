import flet as ft

circles = []  # Definir la lista circles fuera de la función main

def main(page):
    page.title = "Imagen interactiva con Flet"

    # Cargar la imagen PNG del corazón
    heart_image = ft.Image(src="corazon.png")

    # Contenedor principal
    container = ft.Container(
        content=ft.Stack(
            [
                heart_image,
                # Agregar círculos y flechas aquí
                ft.GestureDetector(
                    on_tap=lambda e: toggle_arrow(circles[0]),
                    content=ft.Stack(
                        circles[0],
                        left=100,
                        top=100,
                    ),
                ),
                ft.GestureDetector(
                    on_tap=lambda e: toggle_arrow(circles[1]),
                    content=ft.Stack(
                        circles[1],
                        left=200,
                        top=200,
                    ),
                ),
                # Botón
                ft.ElevatedButton("Botón", on_click=lambda _: print("Botón presionado")),
            ],
            expand=True,
        ),
    )

    page.add(container)

def toggle_arrow(circle):
    if circle[1] is None:
        circle[1] = ft.Icon(ft.icons.ARROW_FORWARD, color="white")
    else:
        circle[1] = None

if __name__ == "__main__":
    circles.append([ft.Circle(color="red", opacity=0.5, scale=0.5), None])
    circles.append([ft.Circle(color="green", opacity=0.5, scale=0.5), None])
    ft.app(target=main)