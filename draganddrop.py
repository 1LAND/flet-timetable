import flet as ft


class DragAndDrop(ft.UserControl):
    def __init__(self,page:ft.Page,*,key:str='One',is_teacher:bool=True,item_size:int=55,group:str='',value:str='',text_size:int = 20,bgcolor=ft.colors.GREEN):
        super().__init__()
        self.page = page
        self.__ref = ft.Ref[ft.Draggable]()
        self.__bgcolor = bgcolor
        self.__group = group
        self.is_teacher = is_teacher
        self.__item_size = item_size
        if key in ["All","One"]:
            self.key = key
        if not value:    
            value = group
        self.__text = ft.Text(value, size=text_size)


    def can_drop(self,table:ft.DataTable,e):
        ...
        

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
        e.control.update()
        self.page.update()

    def build(self):
        if self.is_teacher:
            return ft.Row([ft.Draggable(
                    ref=self.__ref,
                    group=self.__group,
                    content=ft.Container(
                        width=self.__item_size,
                        height=self.__item_size,
                        bgcolor=self.__bgcolor,
                        border_radius=15,
                        content=self.__text,
                        alignment=ft.alignment.center,
                    ),
                    content_feedback=ft.Container(
                                width=20,
                                height=20,
                                bgcolor=self.__bgcolor,
                                border_radius=3,
                                border=ft.border.all(2, ft.colors.BLACK45)
                            ),
                )],
                alignment=ft.MainAxisAlignment.CENTER
                )
        return ft.Row([ft.DragTarget(
                    group=self.__group,
                    content=ft.Container(
                        width=self.__item_size,
                        height=self.__item_size,
                        bgcolor="grey400",
                        content=ft.Text(key=self.key),
                        border_radius=self.__item_size/4,
                        alignment=ft.alignment.center,
                        on_long_press=self.drag_to_default,
                    ),
                    on_accept=self.drag_accept,
                    on_will_accept=self.drag_will_accept,
                    on_leave=self.drag_leave,
                )])
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
        self.__ref
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
    def value(self):
        self.__text
    @value.setter
    def value(self,text):
        self.__text = text
    
    @property
    def group(self):
        return self.__group
    @group.setter
    def group(self,group):
        self.__group = group

    @property
    def item_size(self):
        return self.__item_size
    @group.setter
    def item_size(self,item_size):
        self.__item_size = item_size


if __name__ == '__main__':

    def main(page:ft.Page):
        q = DragAndDrop(page=page)
        page.add(q)
        for i in range(6):
            page.add(q.new_grag_drop())
    ft.app(main)