import flet as ft
class CardiacoNormal():
    def __init__(self,page,navigation_bar,appbar,background_container):
        self.page = page
        self.navigation_bar = navigation_bar
        self.background_container =background_container
        self.appbar = appbar
        self.fotoFondo ='https://i.postimg.cc/Y9R9zHXC/CARDIACO.png'
        self.listAudios = self.InicializarAudios()
        self.lista_audios = []
        self.indice_reproduccion = 0
        self.reproduciendo = False


    def aortico(self,e):
        print("aortico")
        self.ReproducirAud(self.listAudios[0])
    def Triscupideo(self,e):
        print("Triscupideo")
        self.ReproducirAud(self.listAudios[1])
    def Todos(self,e):
        print("Todos")
        for x in self.listAudios:
            self.ReproducirAud(x)
    def Pulmonar(self,e):
        print("Pulmonar")
        self.ReproducirAud(self.listAudios[2])
    def Espacio_de_Erb(self,e):
        print("Espacio_de_Erb")
        self.ReproducirAud(self.listAudios[3])
    def SegmentoInferior(self,e):
        print("SegmentoInferior")
        self.ReproducirAud(self.listAudios[4])

    def getBackground(self):
        background_image = ft.Image(
        src=self.fotoFondo,
        width=self.page.width,
        height=(self.page.height - 20),
        fit=ft.ImageFit.FILL,
        opacity=1,
    )

        return ft.Container(
            content=background_image,
            width=self.page.width,
            height=self.page.height,
            bgcolor='#041114',
            alignment=ft.alignment.top_center,
            
        )
    def getElements(self):
        return ft.Container(
                        content=ft.Row(
                    controls=[ft.Container(
                        ft.Column(
                            controls=[
                                 ft.CupertinoButton(
                            content=ft.Text("aortico - 1", color='#DAEDE8',
                                            text_align=ft.TextAlign.CENTER),
                            bgcolor='#709895',
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(15),
                            opacity_on_click=0.5,
                            on_click=self.aortico,
                            padding=3,
                            width=self.page.width/4),

                             ft.CupertinoButton(
                            content=ft.Text("Triscupideo - 3", color='#DAEDE8',text_align=ft.TextAlign.CENTER),
                            bgcolor='#709895',
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(15),
                            opacity_on_click=0.5,
                            on_click=self.Triscupideo,
                            padding=3,
                            width=self.page.width/4),

                             ft.CupertinoButton(
                            content=ft.Text("Todos", color='#DAEDE8',text_align=ft.TextAlign.CENTER),
                            bgcolor='#709895',
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(15),
                            opacity_on_click=0.5,
                            on_click=self.Todos,
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
                            content=ft.Text("Pulmonar- 2", color='#DAEDE8',text_align=ft.TextAlign.CENTER),
                            bgcolor='#709895',
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(15),
                            opacity_on_click=0.5,
                            on_click=self.Pulmonar,
                            padding=3,
                            width=self.page.width/4),

                             ft.CupertinoButton(
                            content=ft.Text("Espacio_de_Erb - 4", color='#DAEDE8',text_align=ft.TextAlign.CENTER),
                            bgcolor='#709895',
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(15),
                            opacity_on_click=0.5,
                            on_click=self.Espacio_de_Erb,
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
                src="Audio/Cardiacos/AORTICO.mp3",
                autoplay=False,
                volume=1,
                on_state_changed= self.state
                ),
            ft.Audio(
                src="Audio/Cardiacos/TRICUSPIDEO.mp3",
                autoplay=False,
                volume=1,
                on_state_changed= self.state
                ),
            ft.Audio(
                src="Audio/Cardiacos/PULMONAR.mp3",
                autoplay=False,
                volume=1,
                on_state_changed= self.state
                ),
            ft.Audio(
                src= "Audio/Cardiacos/ERB.mp3",
                autoplay=False,
                volume=1,
                on_state_changed= self.state
                ),
            ft.Audio(
                src="Audio/Cardiacos/MITRAL.mp3",
                autoplay=False,
                volume=1,
                on_state_changed= self.state
                )
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

    def getCardiacoNormal(self):
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