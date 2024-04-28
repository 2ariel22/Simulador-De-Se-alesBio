import flet as ft
from views.Resource import Resource

def main(page: ft.Page):
    page.title = "Biopagina"
    page.window_resizable = True
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.padding = 0
    page.bgcolor = '#a5d1c7'
    page.fonts = {
        "zpix": "https://github.com/SolidZORO/zpix-pixel-font/releases/download/v3.1.8/zpix.ttf",
        "stocky": "font/stocky.ttf",
        "Roboto": "font/Roboto-BlackItalic.ttf"
    }
    page.theme = ft.Theme(font_family="Roboto")

    recurso = Resource(page=page)
    recurso.iniciar()
   

ft.app(target=main,view=ft.AppView.WEB_BROWSER)
#ft.app(target=main)