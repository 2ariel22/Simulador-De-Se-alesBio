import flet as ft

color_text = '#192833'
SobreSimuladoText="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse 
et lacus neque. Fusce ultricies, lorem eget elementum cursus, arcu nulla accumsan diam, et 
consequat lacus quam sit amet turpis. Integer efficitur porttitor massa, non hendrerit enim 
pellentesque a. Morbi rutrum lobortis accumsan. Curabitur odio dolor, suscipit nec sapien interdum, 
varius pretium mauris. Nulla fringilla ornare vulputate. Phasellus dapibus eros quam, eu bibendum est 
iaculis nec. Nam porta, mi a scelerisque fermentum, elit sem elementum velit, in sagittis ante velit quis 
turpis. Cras lobortis augue molestie, viverra libero sit amet, scelerisque dui. Nam venenatis cursus risus 
sit amet consectetur. Ut sagittis facilisis diam, ut fermentum dui dignissim sed. Donec feugiat nisl 
non eros porta condimentum. Quisque tellus metus, maximus nec nisi at, dapibus gravida purus. Aliquam
 erat volutpat. Maecenas feugiat ut orci sit amet hendrerit."""

def main(page: ft.Page):
    page.title = "Biopagina"
    page.window_resizable = True
    page.padding = 0
    page.bgcolor = '#90bfd0'
    page.fonts = {
        "zpix": "https://github.com/SolidZORO/zpix-pixel-font/releases/download/v3.1.8/zpix.ttf",
        "stocky":"font/stocky.ttf"
    }
    page.theme = ft.Theme(font_family="zpix")

    titulo = ft.Container(
        ft.Row([
            ft.Container(expand=True),  # Espacio flexible
            ft.Container(
                ft.Text("Simulador", color=color_text,size=25,weight=ft.FontWeight.BOLD),
                
                width=200,  # Ancho del contenedor
                height=50,  # Altura del contenedor
            ),
            ft.Container(expand=True),  # Espacio flexible
        ]),
        padding=20,
    )
    itemsSobrePrograma=ft.Row([
        ft.Image(
        src=f"img/pokemon.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    ),ft.Column([
            ft.Text("Sobre el Simulador", color=color_text,size=20,weight=ft.FontWeight.BOLD,),
            ft.Text(value=SobreSimuladoText,color=color_text,size=15,),
        ]),ft.Image(
        src=f"img/pokemon.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    ),]
    )
    sobre_programa = ft.Container(
        content=itemsSobrePrograma,
        padding=20,
    )

    content = ft.Column(
        controls=[
            titulo,
            sobre_programa,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(content)

ft.app(target=main)