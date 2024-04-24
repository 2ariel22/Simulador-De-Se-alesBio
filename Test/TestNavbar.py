import flet as ft

color_text = '#192833'
fotoCorazon = 'C:/Users/Ariel/Documents/programacion/Luisa/img/4.png'
fotopulmon ='C:/Users/Ariel/Documents/programacion/Luisa/img/3.png'
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

    def navigate(destination: ft.ControlEvent):
        page.scroll = ft.ScrollMode.AUTO
        if destination.data == "0":
            page.views.clear()
            
            page.views.append(
                ft.View(
                    "/explore",
                    [
                        navigation_bar,
                        appbar,
                        ft.Text("Esta es la vista de Explore")
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        elif destination.data == "1":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/commute",
                    [
                        navigation_bar,
                        appbar,
                        ft.Text("Esta es la vista de Commute")
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        else:
            page.views.clear()
            page.views.append(principalView)
        page.update()

    def olaMundo1(e):
        print("ola mundo1")

    def olaMundo2(e):
        print("ola mundo2")

    def olaMundo3(e):
        print("ola mundo3")

    appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MENU),
        title=ft.Text("Simulador de señalesBio"),
        center_title=True,
        bgcolor='#7bdaa7',
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Instagram", on_click=olaMundo1),
                    ft.PopupMenuItem(text="Whasap", on_click=olaMundo2),
                    ft.PopupMenuItem(text="tiktok", on_click=olaMundo3),
                ],
                bgcolor='#a5d1c7'
            )
        ]
    )

    navigation_bar = ft.NavigationBar(
        selected_index=2, bgcolor='#a5d1c7',
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore", data="0"),
            ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute", data="1"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="/",
                data="2"
            ),
        ],
        on_change=navigate
    )

   

    items_sobre_programa = ft.Row(
        [
            ft.Container(width=200, height=200, content=ft.Image(src=fotoCorazon, fit=ft.ImageFit.CONTAIN,border_radius=8)),
            ft.Column(
                [
                    ft.Text("Sobre el Simulador", color=color_text, size=20, weight=ft.FontWeight.BOLD),
                     ft.Container(ft.Text(value=sobre_simulado_text, color=color_text, size=15, text_align=ft.TextAlign.JUSTIFY),border=ft.border.all(color='white',width=4),padding=8,bgcolor=ft.colors.WHITE),
                ],
                
                expand=True,
            ),
            ft.Container(width=100, height=100, content=ft.Image(src=fotopulmon, fit=ft.ImageFit.CONTAIN,border_radius=8)),
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
    

    principalView = ft.View(
        "/",
        [
            navigation_bar,
            appbar,
            sobre_programa,
            imagen_representativa,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER, bgcolor='#a5d1c7',
    )

    
    page.views.append(principalView)
    #page.scroll=ft.ScrollMode
    page.update()

#ft.app(target=main,view=ft.AppView.WEB_BROWSER)
ft.app(target=main)