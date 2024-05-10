import flet as ft

class PaginaSelection():
    def __init__(self,navigation_bar,appbar,background_container,page,control):
        self.navigation_bar = navigation_bar
        self.appbar = appbar
        self.page = page
        self.control = control
        self.background_container = background_container
        self.fotoicon ='https://i.postimg.cc/XN8N04Zr/VENTANA2-PARTE-1.png'
        #self.color_text ='#192833'
        self.fotopulmon ="https://i.postimg.cc/rsQqGN61/VENTANA2-PULMON-PARA-OPCI-N-DE-MEN.png"
        self.fotoCorazon = "https://i.postimg.cc/kGnnthHM/VENTANA2-CORAZ-N-PARA-OPCI-N-DE-MEN.png"
        
        
    
    def AuscultacionCardiaca(self,e):
            
            print("AuscultacionCardiaca")

            self.control.navigate(ft.ControlEvent(data='4',control=None,name=None,page=None,target=None))
    def AuscultacionPulmunar(self,e):
            print("AuscultacionPulmunar")
            self.control.navigate(ft.ControlEvent(data='0',control=None,name=None,page=None,target=None))
    def getPaginaSelection(self):
        textVentana2 ="¿Qué auscultación desea realizar?"
    
        iconImagen =ft.Container(
            ft.Row([
                ft.Column([
                ft.Container(ft.Container(height=self.page.height/3),),
                ft.Image(
            src=self.fotoicon,
            height=300,
            fit=ft.ImageFit.FILL,
            
            
            
            )],expand=True,alignment= ft.VerticalAlignment.END,),
                
            ft.Column([
                ft.Row([ft.Container(ft.Text(value=textVentana2,size=20,color="#DAEDE8",
                                                text_align=ft.TextAlign.CENTER),bgcolor="#457373",padding=15,
                                        expand=True,border_radius=15)],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.Image(
            src=self.fotopulmon,
            height=250,
            fit=ft.ImageFit.FILL,expand=True),
                        ft.Image(
            src=self.fotoCorazon,
            height=250,
            fit=ft.ImageFit.FILL,expand=True)],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.CupertinoButton(
                content=ft.Text("Auscultación pulmonar", color='#DAEDE8',text_align=ft.TextAlign.CENTER),
                bgcolor='#709895',
                alignment=ft.alignment.center,
                border_radius=ft.border_radius.all(15),
                opacity_on_click=0.5,
                on_click=self.AuscultacionPulmunar,
            expand=True,
                padding=3),ft.CupertinoButton(
                content=ft.Text("Auscultación cardiaca", color='#DAEDE8',text_align=ft.TextAlign.CENTER),
                bgcolor='#709895',
                alignment=ft.alignment.center,
                border_radius=ft.border_radius.all(15),
                opacity_on_click=0.5,
                on_click=self.AuscultacionCardiaca,
            expand=True,
                padding=3)],alignment=ft.MainAxisAlignment.CENTER)
                
                ],expand=True,alignment= ft.VerticalAlignment.CENTER,
            
        )],alignment=ft.alignment.center)
            ,margin=10,alignment=ft.alignment.center,expand=True)
        
        
        
        
        medioSelection= ft.Stack([self.background_container,iconImagen])
        
        return ft.View(
            route="/Datos",
            controls=[
                self.navigation_bar,
                medioSelection,
                self.appbar,
            ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        bgcolor= '#a5d1c7',
                        scroll=ft.ScrollMode.AUTO,padding=0,
            
        )
    