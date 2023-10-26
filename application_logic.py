import flet as f


class NavBar(f.UserControl):
    rail = f.NavigationRail(
        selected_index=0,
        label_type=f.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        leading=f.FloatingActionButton(icon=f.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            f.NavigationRailDestination(
                icon=f.icons.FAVORITE_BORDER, selected_icon=f.icons.FAVORITE, label="First"
            ),
            f.NavigationRailDestination(
                icon_content=f.Icon(f.icons.BOOKMARK_BORDER),
                selected_icon_content=f.Icon(f.icons.BOOKMARK),
                label="Second",
            ),
            f.NavigationRailDestination(
                icon=f.icons.SETTINGS_OUTLINED,
                selected_icon_content=f.Icon(f.icons.SETTINGS),
                label_content=f.Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
        height=400
    )
    def build(self):
        nav = f.Row(
            [
                self.rail,
                f.VerticalDivider(width=1),
                f.Column([ f.Text("Body!")], alignment=f.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
        return nav
        

class Table(f.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
        self.start_inscription = f.Container(
            content=f.Column(
                controls=[
                    f.Container(
                        content=f.Text('Добавить расписание',text_align=f.alignment.center),
                        alignment=f.alignment.center,
                    ),
                    f.Container(
                        content=f.FloatingActionButton(
                            icon=f.icons.ADD,
                            on_click=self.init
                            ),
                        alignment=f.alignment.center,
                    )
                ],
                alignment=f.MainAxisAlignment.CENTER,
                height=500,
            ),
        )   

        self.left_bar = NavBar()
    def build(self):
        self.layuot = f.Row(controls=[self.start_inscription])
        return self.layuot
    def init(self,e):
        self.layuot.clean()
        self.page.add(self.left_bar)

def main(page: f.Page):


    dlg = f.AlertDialog(
        title=f.Text("Добавление нового урока"),
        content=f.Column(controls=[
            f.Container(content=
                        f.Row(
                            controls=[lessons,teachers]
                        ),
                    alignment=f.alignment.center,
                    ),
                ],
                height=100
            ),
        actions=[
            f.FloatingActionButton(
                    icon=f.icons.ADD,
                )
        ],
        actions_alignment=f.MainAxisAlignment.END,
        )

    

    layout = Table(page)
    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    page.add(f.ElevatedButton("Open dialog", on_click=open_dlg),layout)
    

f.app(target=main)