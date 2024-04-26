import flet as ft
import webbrowser

color_text = '#192833'
fotoCorazon = "https://i.postimg.cc/kGnnthHM/VENTANA2-CORAZ-N-PARA-OPCI-N-DE-MEN.png"
fotopulmon ="https://i.postimg.cc/rsQqGN61/VENTANA2-PULMON-PARA-OPCI-N-DE-MEN.png"
fotoLogo = 'https://i.postimg.cc/MKxKjXBZ/LOGOPROYECTOSIMULADOR.png'
fotoFondo ='https://i.postimg.cc/HskYYR5B/VENTANA2-FONDO.png'
fotoicon ='https://i.postimg.cc/XN8N04Zr/VENTANA2-PARTE-1.png'

sobre_simulado_text = """¡Bienvenido a la plataforma del simulador de auscultación cardio-pulmonar SymulAus desarrollado por estudiantes de Ingeniería Biomédica de la Universidad Simón Bolívar! Nos complace presentarte una herramienta educativa diseñada para estudiantes , profesionales y entusiastas del área de la salud que desean practicar y mejor sus habilidades en auscultación cardíaca y pulmonar de manera interactiva y efectiva."""

InstagramUrl = "https://www.instagram.com/"
whasapUrl = "https://web.whatsapp.com/"
TiktokUrl = "https://www.tiktok.com/@alyx_tktok/video/7251563513724882181"

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

    def navigate(destination: ft.ControlEvent):
        
        if destination.data == "0":
            page.views.clear()
            
            page.views.append(paginaSelection)
        
        elif destination.data == "1":
            page.views.clear()
            page.views.append(paginaSelection
            )
        else:
            page.views.clear()
            page.views.append(principalView)
        page.update()

    def olaMundo1(e):
        webbrowser.open(InstagramUrl)

    def olaMundo2(e):
        webbrowser.open(whasapUrl)

    def olaMundo3(e):
        webbrowser.open(TiktokUrl)
    

    bienvenida = ft.Row(
    [
        ft.Container(),  # Contenedor vacío para centrar horizontalmente
        ft.Column(
            [
                ft.Image(src=fotoLogo, fit=ft.ImageFit.CONTAIN, border_radius=15,height=300,),
                ft.Text(value=sobre_simulado_text, color=color_text, size=15, text_align=ft.TextAlign.CENTER),
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
            # Alineación horizontal centrada
        ),
        ft.Container(),  # Contenedor vacío para centrar horizontalmente
    ],
    expand=True,alignment= ft.MainAxisAlignment.SPACE_EVENLY,

)

    Imagen_sys = ft.Container(content=bienvenida, expand=True,bgcolor= '#a5d1c7')
    appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MENU),
        title=ft.Text("Symulaus",size=30),
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
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Datos", data="0"),
            ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute", data="1"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Inicio",
                data="2"
            ),
        ],
        on_change=navigate
    )

   

    principalView = ft.View(
                    "/",
                    [
                        navigation_bar,
                        Imagen_sys,
                        appbar,
            
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    bgcolor= '#a5d1c7',
                )
    background_image = ft.Image(
        src=fotoFondo,
        width=page.width,
        height=page.height,
        fit=ft.ImageFit.FILL,
        opacity=1,
    )

    background_container = ft.Container(
        content=background_image,
        width=page.width,
        height=page.height,
        bgcolor='#041114',
        alignment=ft.alignment.center,
        
    )
    textVentana2 ="¿Qué auscultación desea realizar?"
   
    iconImagen =ft.Container(
        ft.Row([
            ft.Column([
            ft.Container(ft.Container(height=page.height/3),),
            ft.Image(
        src=fotoicon,
        height=300,
        fit=ft.ImageFit.FILL,
        
        
        
        )],expand=True,alignment= ft.VerticalAlignment.END,),
            
        ft.Column([
            ft.Row([ft.Container(ft.Text(value=textVentana2,size=20,color="#DAEDE8",
                                              text_align=ft.TextAlign.CENTER),bgcolor="#457373",padding=15,
                                      expand=True,border_radius=15)],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.Image(
        src=fotopulmon,
        height=250,
        fit=ft.ImageFit.FILL,expand=True),
                    ft.Image(
        src=fotoCorazon,
        height=250,
        fit=ft.ImageFit.FILL,expand=True)],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.CupertinoFilledButton(
            content=ft.Text("Auscultación pulmonar"),
            opacity_on_click=0.3,
            on_click=lambda e: print("CupertinoFilledButton clicked!"),
            expand=True,
            padding=3
        ),ft.CupertinoFilledButton(
            content=ft.Text("Auscultación cardiaca"),
            opacity_on_click=0.3,
            on_click=lambda e: print("CupertinoFilledButton clicked!"),
        expand=True,
            padding=3)],alignment=ft.MainAxisAlignment.CENTER)
            
            ],expand=True,alignment= ft.VerticalAlignment.CENTER,
        
    )],alignment=ft.alignment.center)
        ,margin=10,alignment=ft.alignment.center,expand=True)
    
    
    medioSelection= ft.Stack([background_container,iconImagen])
    paginaSelection = ft.View(
        route="/Datos",
        controls=[
            navigation_bar,
            medioSelection,
            appbar,
        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    bgcolor= '#a5d1c7',
                    scroll=ft.ScrollMode.AUTO,padding=0,
        
    )
    
    

    
    page.views.append(principalView)
    
    page.update()

#ft.app(target=main,view=ft.AppView.WEB_BROWSER)
ft.app(target=main)