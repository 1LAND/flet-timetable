import flet as f
import flet_core.control_event 

class ClassBar(f.UserControl):
    def __init__(self,page:f.Page):
        super().__init__()
        self.page = page
        self.add_btn = f.FloatingActionButton(
                icon=f.icons.ADD,
                on_click=self.add_class
                )
        self.layout = f.Column(controls=[],
            width=200,
            horizontal_alignment=f.CrossAxisAlignment.CENTER,
            )
    def build(self):
        self.layout.controls.append(self.add_btn)
        return f.Row([
            self.layout,
            f.VerticalDivider(width=1),
        ])
    def add_class(self,e):
        self.layout.controls.remove(e.control)
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