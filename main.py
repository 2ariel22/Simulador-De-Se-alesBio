import flet as ft

color_text = '#192833'
foto = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwjZ4t-ih4nbCkWprmRCNDb9I3t5bzNEcEeXDtZ9zFoXuf_O0M"
sobre_simulado_text = """¡Bienvenido a la plataforma del simulador de auscultación cardio-pulmonar SymulAus desarrollado por estudiantes de Ingeniería Biomédica de la Universidad Simón Bolívar! Nos complace presentarte una herramienta educativa diseñada para estudiantes , profesionales y entusiastas del área de la salud que desean practicar y mejor sus habilidades en auscultación cardíaca y pulmonar de manera interactiva y efectiva."""

def main(page: ft.Page):
    page.title = "Biopagina"
    page.window_resizable = True
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 0
    page.bgcolor = '#a5d1c7'
    page.fonts = {
        "zpix": "https://github.com/SolidZORO/zpix-pixel-font/releases/download/v3.1.8/zpix.ttf",
        "stocky": "font/stocky.ttf",
        "Roboto": "font/Roboto-BlackItalic.ttf"
    }
    page.theme = ft.Theme(font_family="Roboto")
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore",),
            ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Explore",
            ),
        ])
    def olaMundo1():
        print("ola mundo1")
    def olaMundo2():
        print("ola mundo2")
    def olaMundo3():
        print("ola mundo3")

    # Crear la barra de navegación
    appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MENU),
        title=ft.Text("Simulador de señalesBio"),
        center_title=True,
        bgcolor='#a5d1c7',
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Instagram",on_click=lambda:olaMundo1()),
                    ft.PopupMenuItem(text="Whasap",on_click=lambda:olaMundo2()),
                    ft.PopupMenuItem(text="tiktok",on_click=lambda:olaMundo3()),
                ]
            ,bgcolor='#a5d1c7')
        ]
    )

    # Crear el contenido de la página
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
            ft.Container(width=100, height=100, content=ft.Image(src=foto, fit=ft.ImageFit.CONTAIN)),
            ft.Column(
                [
                    ft.Text("Sobre el Simulador", color=color_text, size=20, weight=ft.FontWeight.BOLD),
                    ft.Container(ft.Text(value=sobre_simulado_text, color=color_text, size=15, text_align=ft.TextAlign.JUSTIFY),border=ft.border.all(color='white',width=4),margin=2),
                ],
                expand=True,  # Permite que el texto se expanda horizontalmente
            ),
            ft.Container(width=100, height=100, content=ft.Image(src=foto, fit=ft.ImageFit.CONTAIN)),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )

    sobre_programa = ft.Container(content=items_sobre_programa, padding=20)

    imagen_representativa = ft.Container(
        content=ft.Image(
            src="https://st2.depositphotos.com/1055484/10070/i/450/depositphotos_100704556-stock-photo-fresh-guava-fruits-on-a.jpg",
            fit=ft.ImageFit.CONTAIN,
            border_radius=8,
        ),
        padding=20,
    )

    content = ft.Column(
        [
            
            sobre_programa,
            imagen_representativa,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Agregar la barra de navegación y el contenido a la página
    page.add(appbar, content)

ft.app(target=main)