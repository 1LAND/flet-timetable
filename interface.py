import flet as ft
from flet_core.user_control import UserControl

class Navigation(UserControl):
    def __init__(self,page: ft.Page):
        super().__init__()
        self.page = page
        self.page.appbar = ft.AppBar(
            leading=ft.Container(
                ft.CircleAvatar(
                    content=ft.Text('user')
                ),
                padding=1,
            ),
            leading_width=40,
            title=ft.Text('LAND'),
            center_title=True,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(
                            text="Checked item", checked=False, 
                        ),
                    ]
                ),
            ],
        )
        self.page.update()
    def build(self):
        return ft.Text('qwe')
        # def __init__(self, page: Page):
    #     self.page = page
    #     self.appbar_items = [
    #         PopupMenuItem(text="Login"),
    #         PopupMenuItem(),  # divider
    #         PopupMenuItem(text="Settings")
    #     ]
    #     self.appbar = AppBar(
    #         leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
    #         leading_width=100,
    #         title=Text("Trolli",size=32, text_align="start"),
    #         center_title=False,
    #         toolbar_height=75,
    #         bgcolor=colors.LIGHT_BLUE_ACCENT_700,
    #         actions=[
    #             Container(
    #                 content=PopupMenuButton(
    #                     items=self.appbar_items
    #                 ),
    #                 margin=margin.only(left=50, right=25)
    #             )
    #         ],
    #     )
    #     self.page.appbar = self.appbar
    #     self.page.update()

def main(page: ft.Page):
        app = Navigation(page)
        page.add(app)
        page.update()
    # page.appbar = ft.AppBar(
    #     leading=ft.Icon(ft.icons.PALETTE),
    #     leading_width=40,
    #     title=ft.Text("AppBar Example"),
    #     center_title=False,
    #     bgcolor=ft.colors.SURFACE_VARIANT,
    #     actions=[
    #         ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
    #         ft.IconButton(ft.icons.FILTER_3),
    #         ft.PopupMenuButton(
    #             items=[
    #                 ft.PopupMenuItem(text="Item 1"),
    #                 ft.PopupMenuItem(),  # divider
    #                 ft.PopupMenuItem(
    #                     text="Checked item", checked=False, 
    #                 ),
    #             ]
    #         ),
    #     ],
    # )

    # page.update()




ft.app(target=main)