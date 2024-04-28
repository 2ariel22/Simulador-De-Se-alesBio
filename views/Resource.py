import flet as ft
import webbrowser
from views.PrincipalView import PrincipalView
from views.PaginaSelection import PaginaSelection
from views.PaginaSelectionTipo import PaginaSelectionTipo


class Resource():
    
    def __init__(self,page):
        self.page = page
        self.fotoFondo ='https://i.postimg.cc/HskYYR5B/VENTANA2-FONDO.png'
        self.InstagramUrl = "https://www.instagram.com/"
        self.whasapUrl = "https://web.whatsapp.com/"
        self.TiktokUrl = "https://www.tiktok.com/@alyx_tktok/video/7251563513724882181"
        self.principalView = PrincipalView(appbar=self.getAppBar(),navigation_bar=self.getNavigation_bar())
    
        self.paginaSelection = PaginaSelection(navigation_bar=self.getNavigation_bar(),
                                      appbar=self.getAppBar(),
                                      background_container=self.getBackground(),
                                      page=self.page)

        self.paginaSelectionTipo = PaginaSelectionTipo(page=self.page,appbar=self.getAppBar(),
                                                 background_container=self.getBackground(),
                                                 navigation_bar=self.getNavigation_bar())
        
    
    def goInstagram(self,e):
        webbrowser.open(self.InstagramUrl)

    def goWhasap(self,e):
        webbrowser.open(self.whasapUrl)

    def goTiktok(self,e):
        webbrowser.open(self.TiktokUrl)
    
    def getAppBar(self):
        return ft.AppBar(
        leading=ft.Icon(ft.icons.MENU),
        title=ft.Text("Symulaus",size=30),
        center_title=True,
        bgcolor='#7bdaa7',
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Instagram", on_click=self.goInstagram),
                    ft.PopupMenuItem(text="whatsapp", on_click=self.goWhasap),
                    ft.PopupMenuItem(text="tiktok", on_click=self.goTiktok),
                ],
                bgcolor='#a5d1c7'
            )
        ]
    )
    
    def navigate(self,destination: ft.ControlEvent):
        
        
        if destination.data == "0":
            self.page.views.clear()
            
            self.page.views.append(self.paginaSelectionTipo.getPaginaSelectionTipo())
        
        elif destination.data == "1":
            self.page.views.clear()
            self.page.views.append(self.paginaSelection.getPaginaSelection()
            )
        else:
            self.page.views.clear()
            self.page.views.append(self.principalView.getPrincipalView())
        self.page.update()

    
    def getNavigation_bar(self):
        return ft.NavigationBar(
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
        on_change=self.navigate
    )
        
    def getBackground(self):
        background_image = ft.Image(
        src=self.fotoFondo,
        width=self.page.width,
        height=self.page.height,
        fit=ft.ImageFit.FILL,
        opacity=1,
    )

        return ft.Container(
            content=background_image,
            width=self.page.width,
            height=self.page.height,
            bgcolor='#041114',
            alignment=ft.alignment.center,
            
        )
        
    def iniciar(self):
        self.page.views.append(self.principalView.getPrincipalView())
    
        self.page.update()