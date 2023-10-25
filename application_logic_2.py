import flet as f
from drop_and_drop import DragAndDrop

class ClassBar(f.UserControl):
    def __init__(self,page:f.Page):
        super().__init__()
        self.page = page
        self.classes = {}
        self.add_btn = f.FloatingActionButton(
                icon=f.icons.ADD,
                on_click=self.add_class
                )
        self.layout = f.Column(controls=[],
            width=150,
            horizontal_alignment=f.CrossAxisAlignment.CENTER,
            )
        self.dlg = f.AlertDialog(
        modal=True,
        title=f.Text("Добавить урок"),
        content=f.Column([
            f.Row([
                f.Dropdown(
                        width=110,
                        options=[
                            f.dropdown.Option("Red"),
                            f.dropdown.Option("Green"),
                            f.dropdown.Option("Blue"),
                        ],
                    ),
                    f.Dropdown(
                        width=110,
                        options=[
                            f.dropdown.Option("Red"),
                            f.dropdown.Option("Green"),
                            f.dropdown.Option("Blue"),
                        ],
                    )
                ]),
        ],
        height=150,
        horizontal_alignment=f.CrossAxisAlignment.CENTER 
        ),
        actions=[
            f.TextButton("Закрыть",on_click=self.close_alert),
            f.FloatingActionButton(icon=f.icons.ADD,), 
        ],
        actions_alignment=f.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    ) 
    def build(self):
        self.layout.controls.append(self.add_btn)
        return f.Row([
            self.layout,
            f.VerticalDivider(width=1),
        ])
    
    def alert_open(self,e):
        self.page.dialog = self.dlg
        self.dlg.open = True
        self.page.update()
    def close_alert(self,e):
        self.dlg.open = False
        self.page.update()

    def add_class(self,e):
        self.alert_open(e)
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