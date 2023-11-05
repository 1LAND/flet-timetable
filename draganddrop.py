import flet as ft


class DragAndDrop(ft.UserControl):
    def __init__(self,page:ft.Page,*,group:str='',text:str='',text_size:int = 20,bgcolor=ft.colors.GREEN):
        super().__init__()
        self.page = page
        self.__ref = ft.Ref[ft.Draggable]()
        self.__bgcolor = bgcolor
        self.__group = group
        if not text:    
            text = group
        self.__text = ft.Text(text, size=text_size)
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
    
    def drag_to_default(self,e):
        e.control.bgcolor = "grey400"
        e.control.content.value = None
        # e.control.control.border = None
        e.control.update()
        self.page.update()
    def build(self):
        return ft.Row([ft.Draggable(
                ref=self.__ref,
                group=self.__group,
                content=ft.Container(
                    width=55,
                    height=55,
                    bgcolor=self.__bgcolor,
                    border_radius=15,
                    content=self.__text,
                    alignment=ft.alignment.center,
                ),
                content_feedback=ft.Container(
                            width=20,
                            height=20,
                            bgcolor=self.__bgcolor+'700',
                            border_radius=3,
                        ),
            )],
            alignment=ft.MainAxisAlignment.CENTER
            )
    def new_grag_drop(self,*,text:str="",key:str|int=0,size:int=20):
        return ft.Row([ft.DragTarget(
                    group=self.__group,
                    content=ft.Container(
                        width=size,
                        height=size,
                        bgcolor="grey400",
                        content=ft.Text(key=key),
                        border_radius=size/4,
                        alignment=ft.alignment.center,
                        on_long_press=self.drag_to_default,
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


if __name__ == '__main__':

    def main(page:ft.Page):
        q = DragAndDrop(page=page)
        page.add(q)
        for i in range(6):
            page.add(q.new_grag_drop())
    ft.app(main)