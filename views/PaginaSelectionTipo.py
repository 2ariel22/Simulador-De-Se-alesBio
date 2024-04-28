import flet as ft


class PaginaSelectionTipo():
    
    def __init__(self,page,navigation_bar,appbar,background_container):
        self.navigation_bar = navigation_bar
        self.appbar = appbar
        self.page = page
        self.background_container = background_container
        self.fotoicon ='https://i.postimg.cc/XN8N04Zr/VENTANA2-PARTE-1.png'
    
    def getPaginaSelectionTipo(self):
        iconImagenTipo =ft.Container(
            ft.Row([
                ft.Column([
                ft.Container(ft.Container(height=self.page.height/3),),
                ft.Image(
            src=self.fotoicon,
            height=300,
            fit=ft.ImageFit.FILL,
            
            
            
            )],expand=True,alignment= ft.VerticalAlignment.END,)]))
        
        medioSelectionTipo= ft.Stack([self.background_container,iconImagenTipo])
        
        return ft.View(
            route="/Datos/Tipo",
            controls=[
                self.navigation_bar,
                medioSelectionTipo,
                self.appbar,
            ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        bgcolor= '#a5d1c7',
                        scroll=ft.ScrollMode.AUTO,padding=0,
            
        )
        