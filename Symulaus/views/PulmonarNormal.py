import flet as ft

class PulmonarNormal():
    def __init__(self,page: ft.Page,navigation_bar,appbar,background_container):
        self.page = page
        self.navigation_bar = navigation_bar
        self.background_container =background_container
        self.appbar = appbar
        self.fotoFondo ='https://i.postimg.cc/rmMs4mNH/PULMONAR.png'
        self.listAudios = self.InicializarAudios()
        self.lista_audios = []
        self.indice_reproduccion = 0
        self.reproduciendo = False


    def Segmento_apical_posterior(self,e):
        print("Segmento_apical_posterior")
        self.ReproducirAud(self.listAudios[0])
    def Segmento_apical(self,e):
        print("Segmento_apical")
        self.ReproducirAud(self.listAudios[1])
    def SegmentoInferior(self,e):
        print("Segmento inferior")
        self.ReproducirAud(self.listAudios[2])
    def Segmento_apical_lobulo_superior(self,e):
        print("Segmento_apical_lobulo_superior")
        self.ReproducirAud(self.listAudios[3])
    def Segmento_apicalDerecho(self,e):
        print("Segmento_apicalDerecho")
        self.ReproducirAud(self.listAudios[4])
    def SegmentoInferiorderecho(self,e):
        print("SegmentoInferiorderecho")
        self.ReproducirAud(self.listAudios[5])

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
    def getElements(self):
        return ft.Container(
                        content=ft.Row(
                    controls=[ft.Container(
                        ft.Column(
                            controls=[
                                 ft.CupertinoButton(
                            content=ft.Text("Segmento apical/posterior - 1", color='#DAEDE8',
                                            text_align=ft.TextAlign.CENTER),
                            bgcolor='#709895',
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(15),
                            opacity_on_click=0.5,
                            on_click=self.Segmento_apical_posterior,
                            padding=3,
                            width=self.page.width/4),

                             ft.CupertinoButton(
                            content=ft.Text("Segmento apical - 3", color='#DAEDE8',text_align=ft.TextAlign.CENTER),
                            bgcolor='#709895',
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(15),
                            opacity_on_click=0.5,
                            on_click=self.Segmento_apical,
                            padding=3,
                            width=self.page.width/4),

                             ft.CupertinoButton(
                            content=ft.Text("Segmento inferior - 5", color='#DAEDE8',text_align=ft.TextAlign.CENTER),
                            bgcolor='#709895',
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(15),
                            opacity_on_click=0.5,
                            on_click=self.SegmentoInferior,
                            padding=3,
                            width=self.page.width/4),
                            
                            ],
                            height=self.page.height/3,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            expand=2,

                            
                        ),margin= ft.margin.only(right=35),
                        expand=2

                    )
                        ,
                        ft.Container(
                            ft.Column(
                            controls=[
                                ft.CupertinoButton(
                            content=ft.Text("Segmento apical / lobulo superior - 2", color='#DAEDE8',text_align=ft.TextAlign.CENTER),
                            bgcolor='#709895',
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(15),
                            opacity_on_click=0.5,
                            on_click=self.Segmento_apical_lobulo_superior,
                            padding=3,
                            width=self.page.width/4),

                             ft.CupertinoButton(
                            content=ft.Text("Segmento apical - 4", color='#DAEDE8',text_align=ft.TextAlign.CENTER),
                            bgcolor='#709895',
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(15),
                            opacity_on_click=0.5,
                            on_click=self.Segmento_apicalDerecho,
                            padding=3,
                            width=self.page.width/4),

                             ft.CupertinoButton(
                            content=ft.Text("Segmento inferior - 6", color='#DAEDE8',text_align=ft.TextAlign.CENTER),
                            bgcolor='#709895',
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(15),
                            opacity_on_click=0.5,
                            on_click=self.SegmentoInferiorderecho,
                            padding=3,
                            width=self.page.width/4,),

                            ],
                            height=self.page.height/3,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            horizontal_alignment=ft.CrossAxisAlignment.END,
                            expand=2,
                        )
                        ,margin= ft.margin.only(left=35),
                        expand=2
                        ),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True
                ),expand=True,
                height=self.page.height,
                alignment=ft.alignment.center,
                
                #margin=ft.margin.only(top=self.page.height/3)
                    )
    def InicializarAudios(self):
        listaAudios = [
            ft.Audio(
                src="Audio/Pulmonares/1.wav",
                autoplay=False,
                volume=1,
                on_state_changed= self.state
                ),
            ft.Audio(
                src="Audio/Pulmonares/2.wav",
                autoplay=False,
                volume=1,
                on_state_changed= self.state
                ),
            ft.Audio(
                src="Audio/Pulmonares/3.wav",
                autoplay=False,
                volume=1,
                on_state_changed= self.state
                ),
            ft.Audio(
                src="Audio/Pulmonares/4.wav",
                autoplay=False,
                volume=1,
                on_state_changed= self.state
                ),
            ft.Audio(
                src="Audio/Pulmonares/5.wav",
                autoplay=False,
                volume=1,
                on_state_changed= self.state
                ),
            ft.Audio(
                src="Audio/Pulmonares/6.wav",
                autoplay=False,
                volume=1,
                on_state_changed= self.state
                ), 
        ]
        for x in listaAudios:
            self.page.overlay.append(x)
        self.page.update()
        return listaAudios

    def ReproducirAud(self, audio):
        self.lista_audios.append(audio)
        if not self.reproduciendo:
            self.reproducir_siguiente()

    def reproducir_siguiente(self):
        if self.indice_reproduccion < len(self.lista_audios):
            self.reproduciendo = True
            audio_actual = self.lista_audios[self.indice_reproduccion]
            audio_actual.play()
            self.indice_reproduccion += 1
        else:
            self.reproduciendo = False
            self.indice_reproduccion = 0

    def state(self, e: ft.ControlEvent):
        
        if e.data == "completed":
            self.reproducir_siguiente()
        


    def getPulmonarNormal(self):
        medioSelectionTipo = ft.Stack([
            self.background_container,
            self.getBackground(),
            self.getElements()
        ])
        return ft.View(
            route="/Datos/Tipo",
            controls=[
                self.navigation_bar,
                medioSelectionTipo,
                self.appbar,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,  # Alineado en la parte inferior
            bgcolor='#a5d1c7',
            scroll=ft.ScrollMode.AUTO,
            padding=0,
        )