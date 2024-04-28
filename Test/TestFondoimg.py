import flet as ft

def xd(width,height):
    background_image = ft.Image(
        src="https://i.postimg.cc/rsQqGN61/VENTANA2-PULMON-PARA-OPCI-N-DE-MEN.png",
        width=width,
        height=height,
        fit=ft.ImageFit.FILL,
        opacity=1,
    )
    background_container = ft.Container(
        content=background_image,
        width=width,
        height=height,
        bgcolor='#041114',
        alignment=ft.alignment.center,
        
    )
    
    
    
    medioSelection= ft.Stack([background_container])
    return ft.View(
        route="/Datos",
        controls=[
            medioSelection,
          ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    bgcolor= '#a5d1c7',
                    scroll=ft.ScrollMode.AUTO,padding=0,
        
    )

def main(page: ft.Page):

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    paginaSelection = xd(page.width,page.height)
    page.views.append(paginaSelection)
    page.update()
    

ft.app(target=main)