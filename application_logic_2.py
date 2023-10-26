import flet as f
from flet import colors
from drop_and_drop import DragAndDrop

class ClassBar(f.UserControl):
    def __init__(self,page:f.Page):
        super().__init__()
        self.page = page
        self.classes = {}
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
                on_click=self.add_class
                )
        self.layout = f.Column(controls=[],
            width=80,
            horizontal_alignment=f.CrossAxisAlignment.CENTER,
            )
        self.dlg = None

    def build(self):
        self.layout.controls.append(self.setting_btn)
        self.layout.controls.append(self.add_btn)
        return f.Row([
            self.layout,
            f.VerticalDivider(width=1),
        ])

    def create_alert(self):    

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
            self.dlg.content.update()

        self.lessons = f.Ref[f.Dropdown]()
        self.teachers = f.Ref[f.Dropdown]()
        self.rooms = f.Ref[f.Dropdown]()

        dict_dropdown = {
            'Уроки':self.lessons,
            'Учителя':self.teachers,
            'Кабинеты':self.rooms,
        }

        list_dropdown = []

        for i in dict_dropdown:
            list_dropdown.append(
                f.Dropdown(
                    ref=dict_dropdown[i],
                    width=150,
                    label=i,
                    options=[
                        f.dropdown.Option('None'),
                    ]
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
                height=200,
                width=225,
                horizontal_alignment=f.CrossAxisAlignment.CENTER 
                ),
                f.Column(controls=[self.color_options],
                width=225,
                height=200,
                )]
            ),
            actions=[
                f.TextButton("Закрыть",on_click=self.close_alert),
                f.FloatingActionButton(icon=f.icons.ADD,), 
            ],
            actions_alignment=f.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        ) 
    def alert_open(self):
        self.page.dialog = self.dlg
        self.dlg.open = True
        self.page.update()
    def close_alert(self,e):
        self.dlg.open = False
        self.page.update()

    def add_class(self,e):
        if not self.dlg:
            self.create_alert()
        self.alert_open()
        # self.classes['A1'] = DragAndDrop(self.page,group='A1')
        # self.classes
        # self.layout.controls.remove(e.control)
        # self.layout.controls.append(self.classes['A1'])
        # self.layout.controls.append(self.add_btn)
        self.update()
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