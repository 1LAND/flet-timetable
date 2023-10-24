import flet as ft


class DragAndDrop(ft.UserControl):
    def __init__(self,page:ft.Page,*,group:str='',text:str='',text_size:int = 20,bgcolor=ft.colors.GREEN):
        super().__init__()
        self.page = page
        self.__ref = ft.Ref[ft.Draggable]()
        self.__bgcolor = bgcolor
        self.__text = ft.Text(text, size=text_size)
        self.__group = group
    def drag_will_accept(self,e):
        e.control.content.border = ft.border.all(
            2, ft.colors.BLACK45 if e.data == "true" else ft.colors.RED
        )
        e.control.update()
    
    def drag_leave(self,e):
        e.control.content.border = None
        e.control.update()
    
    def drag_accept(self,e):
        src = self.page.get_control(e.src_id)
        e.control.content.content.value = src.content.content.value
        e.control.content.bgcolor = src.content.bgcolor
        e.control.content.border = None
        e.control.update()
        self.page.update()
    
    def build(self):
        return ft.Row([ft.Draggable(
                ref=self.__ref,
                group=self.__group,
                content=ft.Container(
                    width=50,
                    height=50,
                    bgcolor=self.__bgcolor,
                    border_radius=5,
                    content=self.__text,
                    alignment=ft.alignment.center,
                ),
                content_feedback=ft.Container(
                            width=20,
                            height=20,
                            bgcolor=self.__bgcolor,
                            border_radius=3,
                        ),
            )])
    def new_grag_drop(self):
        return ft.Row([ft.DragTarget(
                    group=self.__group,
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.BLUE_GREY_100,
                        content=ft.Text(''),
                        border_radius=5,
                        alignment=ft.alignment.center,
                    ),
                    on_accept=self.drag_accept,
                    on_will_accept=self.drag_will_accept,
                    on_leave=self.drag_leave,
                )])

    @property
    def ref(self):
        self.__drag
    @ref.setter
    def ref(self,ref):
        self.ref = ref

    @property
    def bgcolor(self):
        return self.bgcolor
    @bgcolor.getter
    def bgcolor(self,bgcolor):
        self.bgcolor = bgcolor

    @property
    def text(self):
        self.__text
    @text.setter
    def text(self,text):
        self.__text = text
    
    @property
    def group(self):
        return self.__group
    @group.setter
    def group(self,group):
        self.__group = group