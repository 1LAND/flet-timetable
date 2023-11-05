import flet as ft
import random

from admin import ProgrammingPanel
from draganddrop import DragAndDrop

class LBar(ft.UserControl):
    def __init__(self,page:ft.Page,info=''):
        super().__init__()
        self.page = page
        self.components = ft.Ref[ft.Column]()
    def add_teacher(self,e):
        def open_dlg(e):
            self.page.dialog = dlg
            dlg.open = True
            self.page.update()
        def close_dlg(e):
            dlg.open = False
            self.page.update()
        def add_teacher(e):
            colors = [
                "red", "pink","purple","indigo","blue","cyan","lightblue","teal","green","lightgreen","lime","yellow","amber","orange","deeporange","brown","redaccent", "pinkaccent","purpleaccent"]
            if all([dd_lesson.current.value,dd_room.current.value,dd_teacher.current.value]):
                for i in self.components.current.controls[3:]:
                    if f"{dd_teacher.current.value}\n{dd_room.current.value}\n{dd_lesson.current.value}" == i._get_children()[0]._get_children()[0].content.content.value:
                        dd_teacher.current.border_color = "red"    
                        dd_lesson.current .border_color = "red"    
                        dd_room.current   .border_color = "red"    
                        dd_teacher.current.update()
                        dd_lesson.current .update()
                        dd_room.current   .update()
                        return 0

                text=f"{dd_teacher.current.value}\n{dd_room.current.value}\n{dd_lesson.current.value}"
                self.components.current.controls.append(DragAndDrop(self.page,text=text,bgcolor=random.choice(colors)+str(random.randint(6,9))+"00"))
                self.components.current.update()
                close_dlg(e)
            




        dd_teacher = ft.Ref[ft.Dropdown]()
        dd_room    = ft.Ref[ft.Dropdown]()
        dd_lesson  = ft.Ref[ft.Dropdown]()

        dlg = ft.AlertDialog(
            title=ft.Text("Добавить учитель"),
            content=ft.Column([
                    ft.Dropdown(
                        ref=dd_teacher,
                        label="Учитель",
                        width=150,
                        options=[ft.dropdown.Option("АЮ")],
                    ),
                    ft.Dropdown(
                        ref=dd_room,
                        label="Кабинет",
                        width=150,
                        options=[ft.dropdown.Option("307")],
                    ),
                    ft.Dropdown(
                        ref=dd_lesson,
                        label="Предмет",
                        width=150,
                        options=[ft.dropdown.Option("Русский")],
                    ),
                ],
                height=200,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            actions=[
                ft.TextButton("Закрыть",on_click=close_dlg,height=50,),
                ft.FloatingActionButton(
                            content=ft.Icon(ft.icons.ADD),
                            on_click=add_teacher,
                        )

            ],
            actions_alignment=ft.MainAxisAlignment.END
        )   

        open_dlg(e)
    def build(self):
        return ft.Row([ft.Container(
                content=ft.Column(
                    [
                        ft.PopupMenuButton(
                            items=[],
                            icon=ft.icons.SETTINGS,
                        ),
                        ft.FloatingActionButton(
                            content=ft.Icon(ft.icons.ADD),
                            on_click=self.add_teacher,
                        ),
                        ft.Divider(height=1, color="white"),

                    ],
                    ref=self.components,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    ),
                bgcolor="grey900",
                height=self.page.window_height,
                width=100,
                padding=15
            )])

class RBar(ft.UserControl):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page

    def build(self):   
        return ft.Container(
            content=ft.Column([
                    ft.FloatingActionButton(
                            content=ft.Row([
                                ft.Icon(ft.icons.ADD),
                                ft.Text("Добавте табличку",size=20)
                                ], alignment="center", spacing=5),
                            width=250,
                            mini=True,
                            on_click=self.add_table
                        ),
                ],
                width=self.page.window_width-130,
                height=self.page.window_height-90,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            border_radius=10,
            alignment=ft.alignment.center
            )
    def add_table(self,e):
        def open_dlg(e):
            self.page.dialog = dlg
            dlg.open = True
            self.page.update()
        def close_dlg(e):
            dlg.open = False
            self.page.update()
        def add_col_or_row(e):
            ...
        table_name = ft.Ref[ft.TextField]()
        cols = ft.Ref[ft.TextField]()
        rows = ft.Ref[ft.TextField]()
        dlg = ft.AlertDialog(
            title=ft.Text("Добавить табличку"),
            content=ft.Row([
                ft.Column([
                    ft.Text("Конфигурацию таблички",size=20),
                    ft.Column([
                            ft.TextField(
                                ref=cols,
                                label="Название колонки",
                                border_color="white",
                                ),
                            ft.TextField(
                                ref=rows,
                                label="Название строки",
                                border_color="white",
                                ),
                            ft.FloatingActionButton(
                                content=ft.Row([
                                    ft.Icon(ft.icons.ADD),
                                    ft.Text("Добавить элемент",size=20)
                                    ],
                                    alignment="center",
                                    spacing=5),
                                width=300,
                                mini=True,
                                on_click=add_col_or_row
                            ),],
                        height=300,
                        width=300,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Text(""),],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.VerticalDivider(width=10),
            ft.Column([          
                ft.Text("Предпросмотр",size=20),     
                DragAndDrop(self.page,text="Уч",bgcolor="blue900"), 
                ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("")),
                        ft.DataColumn(ft.Text("1")),
                        ft.DataColumn(ft.Text("2")),
                        ft.DataColumn(ft.Text("3")),
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("1A")),
                                ft.DataCell(DragAndDrop(self.page).new_grag_drop(text="УЧ",size=30,)),
                                ft.DataCell(DragAndDrop(self.page).new_grag_drop(text="УЧ",size=30,)),
                                ft.DataCell(DragAndDrop(self.page).new_grag_drop(text="УЧ",size=30,)),
                            ],

                        ),
                    ],
                ),
                ft.Text(),
                ],
                height=300,
                width=400,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ]),
            actions=[
                ft.TextButton("Закрыть",on_click=close_dlg,height=50,),
                ft.TextField(ref=table_name,label="Название таблички",border_color="white",width=300),
                ft.FloatingActionButton(
                    content=ft.Row([
                        ft.Icon(ft.icons.ADD),
                        ft.Text("Добавить табличку",size=20)
                        ],
                    alignment="center",
                    spacing=5,
                    ),
                    width=250
                )
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER
        )

        open_dlg(e)
class TimeTableApp(ft.UserControl):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
    
        self.page.padding = 0
        self.page.spacing = 10

        self.lb = LBar(page)
        self.rb = RBar(page)
        self.admin_panel = ProgrammingPanel(page,lb=self.lb,rb=self.rb)

        self.page.on_keyboard_event = self.admin_panel.keyboard_event
        
    def build(self):
        return ft.Row([
            self.lb,
            self.rb
        ])

def main(page: ft.Page):
    app = TimeTableApp(page)
    page.add(app)

ft.app(target=main)