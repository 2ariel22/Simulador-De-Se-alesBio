import flet as ft


class PrincipalView():
    
    def __init__(self,navigation_bar,appbar):
        self.navigation_bar = navigation_bar
        self.appbar = appbar
        self.fotoLogo = 'https://i.postimg.cc/MKxKjXBZ/LOGOPROYECTOSIMULADOR.png'
        self.sobre_simulado_text="""¡Bienvenido a la plataforma del simulador de auscultación cardio-pulmonar SymulAus desarrollado por estudiantes de Ingeniería Biomédica de la Universidad Simón Bolívar! Nos complace presentarte una herramienta educativa diseñada para estudiantes , profesionales y entusiastas del área de la salud que desean practicar y mejor sus habilidades en auscultación cardíaca y pulmonar de manera interactiva y efectiva."""
        self.color_text ='#192833'
    
    def getPrincipalView(self):
        bienvenida = ft.Row(
        [
            ft.Container(),  # Contenedor vacío para centrar horizontalmente
            ft.Column(
                [
                    ft.Image(src=self.fotoLogo, fit=ft.ImageFit.CONTAIN, border_radius=15,height=300,),
                    ft.Text(value=self.sobre_simulado_text, color=self.color_text, size=15, text_align=ft.TextAlign.CENTER),
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
        
        return ft.View(
                        "/",
                        [
                            self.navigation_bar,
                            Imagen_sys,
                            self.appbar,
                
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        bgcolor= '#a5d1c7',
                    )
    