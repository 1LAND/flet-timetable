import flet as ft


class BaseInfo:
    def __init__(self,page:ft.Page=None,*,size:int=40,bgcolor=ft.colors.GREEN,text:str="Уч",text_size:int=10) -> None:
        self.page = page
        self.__size = size
        self.__border_radius = self.__size*0.3
        self.__bgcolor =  bgcolor
        self.__text_size = text_size
        self.__text = ft.Text(text,size=self.__text_size)     

    @property
    def bgcolor(self):
        return self.__bgcolor
    @bgcolor.setter
    def bgcolor(self,bgcolor):
        self.__bgcolor = bgcolor

    @property
    def border_radius(self):
        return self.__border_radius
    @border_radius.setter
    def border_radius(self,size):
        self.__border_radius = size

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self,size):
        self.__size = size
 
    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self,text):
        self.__text.value = text

    @property
    def text_size(self):
        return self.__text_size
    @text_size.setter
    def text_size(self,text_size):
        self.__text_size = text_size   

class Teacher(ft.UserControl,BaseInfo):
    def __init__(self,page:ft.Page,teacher_name:str='',*,lessons:list=[]):
        super().__init__()
        self.page = page

        self.__lessons = lessons
        if teacher_name:
            self.text = teacher_name
    def build(self):
        return ft.Row(
            controls=[
                ft.Draggable(
                    content=ft.Container(
                        width=self.size,
                        height=self.size,
                        bgcolor=self.bgcolor,
                        border_radius=self.border_radius,
                        alignment=ft.alignment.center,
                        content=self.text
                    ),
                    content_feedback=ft.Container(
                        width=self.size/2,
                        height=self.size/2,
                        bgcolor=self.bgcolor,
                        border_radius=self.border_radius/2,
                        border=ft.border.all(2, ft.colors.BLACK45)
                    ),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER)
    @property
    def lessons(self):
        return self.__lessons
    @lessons.setter
    def lessons(self,lesson):
        self.__lessons.append(lesson)
        self.__lessons.sort()
class CellForTeacher(ft.UserControl,BaseInfo):
    def __init__(self,page,lesson:tuple,teachers:list=[]):
        super().__init__()
        self.page = page
        self.lesson = lesson
        self.teachers = teachers
        self.teacher:Teacher = None 
    def can_take_teacher(self,teacher, mode='default'):
        try:
            if mode == "default":
                return not teacher.lessons or not self.lesson[0] in teacher.lessons
            elif mode == "all":
                return True
        except AttributeError:
            return False

    def to_default(self,e):
        e.control.bgcolor = "grey400"
        e.control.content.value = None
        e.control.update()
        self.page.update()
    def to_accept(self,e):
        if self.can_take_teacher(self.teacher):
            self.teacher.lessons.append(self.lesson[0])
            self.teacher = None
            teacher_container = self.page.get_control(e.src_id)
            e.control.content.bgcolor = teacher_container.content.bgcolor
            e.control.content.content.value=teacher_container.content.content.value
        e.control.content.border = None
        e.control.update()
    
    def to_will_accept(self,e):
        for teacher in self.teachers:
            print(teacher.text,teacher.lessons)
            if self.can_take_teacher(teacher):
                self.teacher = teacher
                e.control.content.border = ft.border.all(2, ft.colors.BLACK45)
                break
            else:
                e.control.content.border = ft.border.all(2,ft.colors.RED)
        e.control.update()
    def to_leave(self,e):
        e.control.content.border = None
        e.control.update()
    
    def build(self):
        return ft.Row([ft.DragTarget(
                    content=ft.Container(
                        width=self.size,
                        height=self.size,
                        bgcolor="grey400",
                        border_radius=self.border_radius,
                        alignment=ft.alignment.center,
                        content=ft.Text(),
                        on_long_press=self.to_default,
                    ),
                    on_accept=self.to_accept,
                    on_will_accept=self.to_will_accept,
                    on_leave=self.to_leave,
                )])
class DragAndDrop(ft.UserControl):
    def __init__(self,page:ft.Page,*,key:str='One',is_teacher:bool=True,list_teachers:list=[],item_size:int=55,value:str='',text_size:int = 20,bgcolor=ft.colors.GREEN):
        super().__init__()
        self.page = page
        self.__ref = ft.Ref[ft.Draggable]()
        self.__bgcolor = bgcolor
        self.is_teacher = is_teacher
        if not self.is_teacher:
            self.list_teachers = list_teachers
        self.__item_size = item_size
        self.key = key 
        self.__text = ft.Text(value, size=text_size)
    
    def drag_will_accept(self,e:ft.ControlEvent):
        for el in self.list_teachers:
            if self.key[1]  in el.key:
                e.control.content.border = ft.border.all(2, ft.colors.BLACK45)
            else:
                e.control.content.border = ft.border.all(2, ft.colors.RED)
        e.control.update()
    
    def drag_leave(self,e):
        e.control.content.border = None
        e.control.update()
    
    def drag_accept(self,e):
        src = self.page.get_control(e.src_id)
        for el in self.list_teachers:
            if ...:
                el.key[self.key[1]-1]=self.key 
                e.control.content.bgcolor = src.content.bgcolor
                e.control.content.value = src.content.content.value
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
    @property
    def ref(self):
        self.__ref
    @ref.setter
    def ref(self,ref):
        self.ref = ref

    @property
    def bgcolor(self):
        return self.bgcolor
    @bgcolor.setter
    def bgcolor(self,bgcolor):
        self.bgcolor = bgcolor

    @property
    def value(self):
        self.__text
    @value.setter
    def value(self,text):
        self.__text = text
    
    @property
    def item_size(self):
        return self.__item_size

if __name__ == '__main__':
    def main(page:ft.Page):
        t1 = Teacher(page,'AЮ')
        t1 = Teacher(page,'ХУЙ')
        tl = [t1,t2]
        page.add(ft.Row([t1,t2]))
        
        col1 = ft.Column()
        for i in range(4):
            col1.controls.append(CellForTeacher(page,lesson=(i+1,'11d'),teachers=tl))
        col2 = ft.Column()
        for i in range(4):
            col2.controls.append(CellForTeacher(page,lesson=(i+1,'2a'),teachers=tl))
        page.add(ft.Row([col1,col2])) 
    ft.app(main)