import flet as ft

def main(page: ft.Page):
    page.padding=0
    background_image = ft.Image(
        src="img/Test1.png",
        width=page.width,
        height=page.height,
        fit=ft.ImageFit.FILL,
    )

    background_container = ft.Container(
        content=background_image,
        width=page.width,
        height=page.height,
        bgcolor=ft.colors.TRANSPARENT,
        alignment=ft.alignment.center,
    )

    page.add(background_container)
    page.update()


ft.app(target=main)