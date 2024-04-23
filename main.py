import flet as ft

color_text = '#192833'
sobre_simulado_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse et lacus neque. Fusce ultricies, lorem eget elementum cursus, arcu nulla accumsan diam, et consequat lacus quam sit amet turpis. Integer efficitur porttitor massa, non hendrerit enim pellentesque a. Morbi rutrum lobortis accumsan. Curabitur odio dolor, suscipit nec sapien interdum, varius pretium mauris. Nulla fringilla ornare vulputate. Phasellus dapibus eros quam, eu bibendum est iaculis nec. Nam porta, mi a scelerisque fermentum, elit sem elementum velit, in sagittis ante velit quis turpis. Cras lobortis augue molestie, viverra libero sit amet, scelerisque dui. Nam venenatis cursus risus sit amet consectetur. Ut sagittis facilisis diam, ut fermentum dui dignissim sed. Donec feugiat nisl non eros porta condimentum. Quisque tellus metus, maximus nec nisi at, dapibus gravida purus. Aliquam erat volutpat. Maecenas feugiat ut orci sit amet hendrerit."""

def main(page: ft.Page):
    page.title = "Biopagina"
    page.window_resizable = True
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 0
    page.bgcolor = '#90bfd0'
    page.fonts = {
        "zpix": "https://github.com/SolidZORO/zpix-pixel-font/releases/download/v3.1.8/zpix.ttf",
        "stocky": "font/stocky.ttf",
        "Roboto": "font/Roboto-BlackItalic.ttf"
    }
    page.theme = ft.Theme(font_family="Roboto")

    titulo = ft.Row(
        [
            ft.Container(width=0, expand=True),
            ft.Text("Simulador de señalesBio", color=color_text, size=25, weight=ft.FontWeight.BOLD),
            ft.Container(width=0, expand=True),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        height=70,
    )

    items_sobre_programa = ft.Row(
        [
            ft.Container(width=100, height=100, content=ft.Image(src=f"https://w7.pngwing.com/pngs/732/154/png-transparent-pokemon-meowth-whiskers-meowth-pokemon-go-ash-ketchum-pokemon-go-mammal-cat-like-mammal-carnivoran-thumbnail.png", fit=ft.ImageFit.CONTAIN)),
            ft.Column(
                [
                    ft.Text("Sobre el Simulador", color=color_text, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(value=sobre_simulado_text, color=color_text, size=15, text_align=ft.TextAlign.JUSTIFY),
                ],
                expand=True,  # Permite que el texto se expanda horizontalmente
            ),
            ft.Container(width=100, height=100, content=ft.Image(src=f"https://github.com/2ariel22/Simulador-De-Se-alesBio/blob/master/img/pokemon.png?raw=true", fit=ft.ImageFit.CONTAIN)),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )

    sobre_programa = ft.Container(content=items_sobre_programa, padding=20)

    imagen_representativa = ft.Container(
        content=ft.Image(
            src=f"https://st2.depositphotos.com/1055484/10070/i/450/depositphotos_100704556-stock-photo-fresh-guava-fruits-on-a.jpg",
            fit=ft.ImageFit.CONTAIN,
            border_radius=8,
        ),
        padding=20,
    )

    content = ft.Column(
        [
            titulo,
            sobre_programa,
            imagen_representativa,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(content)

ft.app(target=main)