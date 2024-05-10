import flet as ft



class PaginaSelectionTipo():
    
    def __init__(self,page: ft.Page,navigation_bar,appbar,background_container,control):
        self.navigation_bar = navigation_bar
        self.appbar = appbar
        self.page = page
        self.control = control
        self.background_container = background_container
        self.fotoicon ='https://i.postimg.cc/XN8N04Zr/VENTANA2-PARTE-1.png'
        self.ondaSon = 'https://i.postimg.cc/PJqq6Rcz/onda.png'
        self.colorText = '#DAEDE8'
        self.tipo = None
        
    
    def soundNormal(self,e):
            print("Sonido Normal")
            self.control.navigate(ft.ControlEvent(data=self.tipo,control=None,name=None,page=None,target=None))
    def soundAnormal(self,e):
            print("Sonido Anormal")
    
    def getPaginaSelectionTipo(self,tipo):
        self.tipo = tipo
        iconImagenTipo = ft.Container(
            ft.Column(controls=[
                ft.Row(controls=[
                    ft.Column(controls=[
                        
                        ft.Image(
                            src=self.ondaSon,
                            height=200,
                        ),
                        ft.CupertinoButton(
                            content=ft.Text("Normal", color='#DAEDE8',text_align=ft.TextAlign.CENTER),
                            bgcolor='#709895',
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(15),
                            opacity_on_click=0.5,
                            on_click=self.soundNormal,
                            padding=3,
                            width=self.page.width/3),
                        
                    ],expand=1),
                    ft.Column(controls=[
                        ft.Container(content=ft.Text("¿Qué sonidos desea evaluar?",color=self.colorText),
                                     padding=20,
                                     bgcolor='#457373',margin=5,
                                     border_radius=15),
                        ft.Image(
                            src=self.fotoicon,
                            fit=ft.ImageFit.FILL,
                        ),
                        
                    ],expand=2,horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.Column(controls=[
                        
                        ft.Image(
                            src=self.ondaSon,
                            height=200,
                        ),
                        ft.CupertinoButton(
                            content=ft.Text("Anormal", color='#DAEDE8',text_align=ft.TextAlign.CENTER),
                            bgcolor='#709895',
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(15),
                            opacity_on_click=0.5,
                            on_click=self.soundAnormal,
                            padding=3,
                            width=self.page.width/3),
                        
                        
                    ],expand=1)
                ])
            ],alignment=ft.MainAxisAlignment.SPACE_EVENLY),
            width=self.page.width,
            height=self.page.height,
            margin=5
            
        )

        medioSelectionTipo = ft.Stack([
            self.background_container,
            iconImagenTipo
        ])

        return ft.View(
            route="/Datos/Tipo",
            controls=[
                self.navigation_bar,
                medioSelectionTipo,
                self.appbar,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.END,  # Alineado en la parte inferior
            bgcolor='#a5d1c7',
            scroll=ft.ScrollMode.AUTO,
            padding=0,
        )
        