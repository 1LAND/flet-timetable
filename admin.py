import flet as f
from flet_core.control import Control

class ProgrammingPanel(Control):  
    def __init__(self,page:f.Page,**admin_dict) -> None:
        self.page = page
        self.text_code = f.Ref[f.TextField]()
        self.admin_func_dict = admin_dict

    def build(self):
        return super().build()
    
    def do_code(self,e):
        try:
            exec(self.text_code.current.value,self.admin_func_dict)
        except Exception as err:
            self.err_text.current.value = err
            self.text_code.current.border_color = f.colors.RED_900
            self.page.update()
        else:
            self.create_banner(f'function Accept: {self.text_code}, {self.text_code.current.value}',[f.TextButton("Cancel", on_click=self.close_banner)])
            self.open_banner(e)
    def create_dlg(self):
        self.err_text = f.Ref[f.Text]()
        self.dlg = f.AlertDialog(
            title=f.Text("Panel Programming"),
            modal=False,
            content=f.Column([
                f.Text('',ref=self.err_text,color=f.colors.RED_900),
                f.Row(
                controls=[
                    f.TextField(ref=self.text_code,multiline=True,autofocus=True),
                    f.FloatingActionButton(icon=f.icons.ADD,on_click=self.do_code,)
                ],
                width=400,
                ),
            ],
            height=100),
            actions=[]
            )
        return self.dlg
    def open_dlg(self,e):
        self.create_dlg()
        self.page.dialog = self.dlg
        self.page.dialog.open = True
        self.page.update()
    def close_dlg(self,e): 
        self.page.dialog = False
        self.page.update()

    def create_banner(self,banner_text:str,btns:list):
        self.ban = f.Banner(
            bgcolor=f.colors.BLUE_300,
            leading=f.Icon(f.icons.INFO, color=f.colors.BLUE, size=40),
            content=f.Text(banner_text,color=f.colors.BLUE,size=20),
            actions=btns
        )
        return self.ban
    def close_banner(self,e):
        self.page.banner.open = False
        self.page.update()

    def open_banner(self,e):
        self.page.banner = self.ban
        self.page.banner.open = True
        self.page.update()

    def keyboard_event(self,e: f.KeyboardEvent):
        if e.shift and e.key == '~':
            self.open_dlg(e)

if __name__ == '__main__':
    def main(page:f.Page):
        pp = ProgrammingPanel(page)
        page.on_keyboard_event = pp.keyboard_event
        page.update()
    f.app(main)

        