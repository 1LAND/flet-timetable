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
                self.components.current.controls.append(DragAndDrop(self.page,value=text,bgcolor=random.choice(colors)+str(random.randint(6,9))+"00",text_size=10))
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

    

    def add_row(self,table:ft.DataTable,row:str):
        if len(table.rows) == 1 and table.rows[0].cells[0].content.value == '':
            table.rows[0].cells[0].content.value = row
            table.rows[0].cells[0].content.update()
            table.update()
            self.page.update()
            return False 
        for i in table.rows:
            if i.cells and i.cells[0].content.value == row: return False
        data_row = ft.DataRow()
        for i in range(len(table.columns)):
            if i == 0:
                data_row.cells.append(ft.DataCell(ft.Text(row)))
            else:
                data_row.cells.append(ft.DataCell(DragAndDrop(self.page,is_teacher=False,item_size=30)))
        table.rows.append(data_row)
        table.update()
        self.page.update()
        return True
    def add_col(self,table:ft.DataTable,col:str):
        if not table.columns:
            table.columns.append(ft.DataColumn(ft.Text('')))
            table.rows[-1].cells.append(ft.DataCell(ft.Text('')))
            table.columns.append(ft.DataColumn(ft.Text(col)))
            table.rows[-1].cells.append(DragAndDrop(self.page,is_teacher=False,item_size=30))
            table.update()
            self.page.update()
            return False
        for i in table.columns:
            if i.label.value == col: return False
        # if not table.columns:
        #     table.columns.append(ft.DataColumn(ft.Text('')))
        table.columns.append(ft.DataColumn(ft.Text(col)))
        for i in table.rows:
            if len(i.cells) != len(table.columns):
                i.cells.append(ft.DataCell(DragAndDrop(self.page,is_teacher=False,item_size=30)))
        table.update()
        self.page.update()
        return True
    def add_table(self,e):
        def open_dlg(e):
            self.page.dialog = dlg
            dlg.open = True
            self.page.update()
        def close_dlg(e):
            dlg.open = False
            self.page.update()
        def add_col_or_row(e):
            if cols.current.value:
                if self.add_col(table.current,cols.current.value):
                    if isinstance(dlg.content.controls[-1].width,int):
                        dlg.content.controls[-1].width += 100
                        dlg.content.controls[-1].update()
                    rows.current.disabled = False
                    rows.current.update()
                    self.page.update()
            if rows.current.value:
                self.add_row(table.current,rows.current.value)
        table_name = ft.Ref[ft.TextField]()
        cols = ft.Ref[ft.TextField]()
        rows = ft.Ref[ft.TextField]()
        table = ft.Ref[ft.DataTable]()

        dlg = ft.AlertDialog(
            title=ft.Text("Добавить табличку"),
            content=
                ft.Row([
                    ft.Column([
                            ft.Text("Конфигурацию таблички",size=20),
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
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.VerticalDivider(width=10),      
                ft.Column(
                    controls=[
                        ft.Text("Предпросмотр",size=20),  
                        DragAndDrop(self.page,value="Уч",bgcolor="blue900"), 
                        ft.DataTable(
                            ref=table,
                            columns=[
                                # ft.DataColumn(ft.Text("")),
                                # ft.DataColumn(ft.Text("1")),
                                # ft.DataColumn(ft.Text("2")),
                                # ft.DataColumn(ft.Text("3")),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        # ft.DataCell(ft.Text("11A")),
                                        # ft.DataCell(DragAndDrop(self.page,is_teacher=False,item_size=30)),
                                        # ft.DataCell(DragAndDrop(self.page,is_teacher=False,item_size=30)),
                                        # ft.DataCell(DragAndDrop(self.page,is_teacher=False,item_size=30)),
                                    ],

                                ),
                            ],
                        ),
                    ],
                    scroll=ft.ScrollMode.ALWAYS,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    auto_scroll=True),
                ],
                scroll=ft.ScrollMode.ALWAYS,
                auto_scroll=True,
                height=400),
            actions=[
                ft.TextButton("Закрыть",on_click=close_dlg,height=50,),
                ft.TextField(ref=table_name,label="Название таблички",border_color="white",width=250),
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