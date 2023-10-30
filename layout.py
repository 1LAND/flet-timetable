import flet as f
import pandas as pd

class LayoutTable(f.UserControl):
    def __init__(self,page:f.Page,*,table_info:str=""):
        super().__init__()
        self.page = page
        if table_info:
            self.table_info = pd.read_csv(table_info,sep=";",encoding="cp1251")
        else:
            self.table_info = pd.DataFrame(index=None)

        self.row = f.Row(alignment=f.MainAxisAlignment.CENTER)

        self.init()
    def build(self):
        return self.row 
    
    def init(self):
        if not self.table_info.size:
            self.row.controls.append(
                f.Column([
                    f.Text("Создайте табличку"),
                    f.FloatingActionButton(icon=f.icons.ADD,on_click=self.add_table)
                ],
                horizontal_alignment=f.CrossAxisAlignment.CENTER,
                alignment=f.MainAxisAlignment.CENTER,
                height=self.page.window_height-100
                )
            )

    def add_table(self,e):
        def open_table_dialog(e):
            self.page.dialog = self.create_table_dialog
            self.create_table_dialog.open = True
            self.page.update()
        def close_table_dialog(e):
            self.create_table_dialog.open = False
            self.page.update()

        def on_hover(e):
            e.control.bgcolor = "blue900" if e.data == "true" else "grey"
            e.control.update()

        grid = f.GridView(
                expand=1,
                runs_count=5,
                max_extent=30,
                child_aspect_ratio=1.0,
                spacing=5,
                run_spacing=5,
            )

        for i in range(0,49):
            grid.controls.append(
                f.Container(bgcolor="grey", on_hover=on_hover,border_radius=f.border_radius.all(10),on_long_press=lambda x: print('asd'))
            )
        self.page.update()

        self.create_table_dialog = f.AlertDialog(
            modal=True,
            title=f.Text("Please confirm"),
            content=grid,
            actions_alignment=f.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        open_table_dialog(e)
if __name__ == '__main__':
    
    def main(p:f.Page):p.add(LayoutTable(p))

    f.app(main)