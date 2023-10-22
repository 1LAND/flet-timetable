import flet as f


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
                            on_click=self.clear_all_table
                            ),
                        alignment=f.alignment.center,
                    )
                ],
                alignment=f.MainAxisAlignment.CENTER,
                height=500,
            ),
        )
    def build(self):
        self.layuot = f.Stack(controls=[self.start_inscription])
        return self.layuot
    def create_col(self,*e):
        # dlg_modal = f.AlertDialog(
        #         modal=True,
        #         title=f.Text("Please confirm"),
        #         content=f.Text("Do you really want to delete all those files?"),
        #         actions=[
        #             f.TextButton("Yes", on_click=close_dlg),
        #             f.TextButton("No", on_click=close_dlg),
        #         ],
        #         actions_alignment=ft.MainAxisAlignment.END,
        #         on_dismiss=lambda e: print("Modal dialog dismissed!"),
        #     )
        ...
    def clear_all_table(self,e):
        self.layuot.clean()
        self.page.update()


def main(page: f.Page):

    lessons = f.Dropdown(
        width=120,
        label='Уроки',
        options=[
            f.dropdown.Option('None'),
        ],
    )
    teachers = f.Dropdown(
        width=120,
        label='Учителя',
        options=[
            f.dropdown.Option('None'),
        ],
    )


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