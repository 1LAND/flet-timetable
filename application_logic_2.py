import flet as f
from flet import colors
from functools import partial
from drop_and_drop import DragAndDrop
from secret_code import keyboard_event


class ClassBar(f.UserControl):
    def __init__(self,page:f.Page):
        super().__init__()
        self.page = page
        self.setting_btn = f.PopupMenuButton(
                items=[
                f.PopupMenuItem(text="Item 1"),
                f.PopupMenuItem(icon=f.icons.POWER_INPUT, text="Check power"),
                f.PopupMenuItem(
                    content=f.Row(
                        [
                            f.Icon(f.icons.HOURGLASS_TOP_OUTLINED),
                            f.Text("Item with a custom content"),
                        ]
                    ),
                    on_click=lambda _: print("Button with a custom content clicked!"),
                ),
                f.PopupMenuItem(),  # divider
                f.PopupMenuItem(
                    text="Checked item", checked=False, 
                ),
            ]
        )
        self.add_btn = f.FloatingActionButton(
                icon=f.icons.ADD,
                on_click=self.open_alert,
                )
        self.layout = f.Column(controls=[],
            width=80,
            horizontal_alignment=f.CrossAxisAlignment.CENTER,
            )
        self.dlg = None
        self.cells = []
        self.cell = {
            'lessons':None,
            'teachers':None,
            'classes':None,
            'rooms':None,
            'color':None,
        }
        self.lessons_list = []
        self.teachers_list = []
        self.classes_list = []
        self.rooms_list = []
        self.page.on_keyboard_event=partial(keyboard_event,self.page,self)
   
    def build(self):
        self.layout.controls.append(self.setting_btn)
        self.layout.controls.append(self.add_btn)
        return f.Row([
            self.layout,
            f.VerticalDivider(width=1),
        ])

    def create_alert(self):    
        
        def try_add_cell(e):
            if all([self.lessons.current.value, 
                self.teachers.current.value,
                self.rooms.current.value,
                self.classes.current.value]):
                self.close_alert(e)    

        def dropdown_changed(e):
            self.cell['lessons'] = self.lessons.current.value
            self.cell['teachers'] = self.teachers.current.value
            self.cell['classes'] = self.classes.current.value
            self.cell['rooms'] = self.rooms.current.value
        def color_option_creator(color: str):
            return f.Container(
                bgcolor=color,
                border_radius=f.border_radius.all(50),
                height=10,
                width=10,
                padding=f.padding.all(5),
                alignment=f.alignment.center,
                data=color
            )

        def set_color(e):
            self.color_options.data = e.control.data
            for k, v in option_dict.items():
                if k == e.control.data:
                    v.border = f.border.all(3, colors.BLACK26)
                else:
                    v.border = None
            self.cell['color'] = self.color_options.data
            self.dlg.content.update()


        self.lessons = f.Ref[f.Dropdown]()
        self.teachers = f.Ref[f.Dropdown]()
        self.classes = f.Ref[f.Dropdown]()
        self.rooms = f.Ref[f.Dropdown]()

        dict_dropdown = {
            'Уроки':[self.lessons,self.lessons_list],
            'Учителя':[self.teachers,self.teachers_list],
            'Кабинеты':[self.rooms,self.rooms_list],
            'Класс':[self.classes,self.classes_list],
        }

        list_dropdown = []

        for i in dict_dropdown:
            list_dropdown.append(
                f.Dropdown(
                    ref=dict_dropdown[i][0],
                    width=150,
                    label=i,
                    options=dict_dropdown[i][1],
                    on_change=dropdown_changed
                )
            )

        
        self.color_options = f.GridView(runs_count=3, max_extent=40, data="", height=150)


        option_dict = {
            colors.LIGHT_GREEN: color_option_creator(colors.LIGHT_GREEN),
            colors.RED_200: color_option_creator(colors.RED_200),
            colors.AMBER_500: color_option_creator(colors.AMBER_500),
            colors.PINK_300: color_option_creator(colors.PINK_300),
            colors.ORANGE_300: color_option_creator(colors.ORANGE_300),
            colors.LIGHT_BLUE: color_option_creator(colors.LIGHT_BLUE),
            colors.DEEP_ORANGE_300: color_option_creator(colors.DEEP_ORANGE_300),
            colors.PURPLE_100: color_option_creator(colors.PURPLE_100),
            colors.RED_700: color_option_creator(colors.RED_700),
            colors.TEAL_500: color_option_creator(colors.TEAL_500),
            colors.YELLOW_400: color_option_creator(colors.YELLOW_400),
            colors.PURPLE_400: color_option_creator(colors.PURPLE_400),
            colors.BROWN_300: color_option_creator(colors.BROWN_300),
            colors.CYAN_500: color_option_creator(colors.CYAN_500),
            colors.BLUE_GREY_500: color_option_creator(colors.BLUE_GREY_500),
        }

        for _, v in option_dict.items():
            v.on_click = set_color
            self.color_options.controls.append(v)

        self.dlg = f.AlertDialog(
            modal=True,
            title=f.Text("Добавить урок"),
            content=f.Row(
                [f.Column(
                controls=list_dropdown,
                height=230,
                width=225,
                horizontal_alignment=f.CrossAxisAlignment.CENTER 
                ),
                f.Column(controls=[self.color_options],
                width=225,
                height=230,
                alignment=f.MainAxisAlignment.CENTER
                )],
            ),
            actions=[
                f.TextButton("Закрыть",on_click=self.close_alert),
                f.FloatingActionButton(
                    icon=f.icons.ADD,
                    on_click=try_add_cell
                ), 
            ],
            actions_alignment=f.MainAxisAlignment.END,
        ) 
    def open_alert(self,e):
        if not self.dlg:
            self.create_alert()
        self.page.dialog = self.dlg
        self.dlg.open = True
        self.page.update()
    def close_alert(self,e):
        self.dlg.open = False
        self.page.update()
    def add_cell(self,e):
        print(self.cell)

    def add_on_dd_list(self,list:list,elem:str):
        list.append(f.dropdown.Option(elem))

def main(page: f.Page): 

    page.add(
        f.Row(
            [
                ClassBar(page),
                f.Column([ f.Text("Body!")], alignment=f.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )

f.app(target=main)