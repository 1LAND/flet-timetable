import flet as ft
from flet_core.user_control import UserControl
from flet_core.template_route import TemplateRoute


class Layout(ft.Row):
    def _init__(self,app,  page: ft.Page):
        super().__init__()
        self.app = app
        self.page = page
        self.rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            # extended=True,
            min_width=100,
            min_extended_width=400,
            leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                    selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                    label="Second",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                    label_content=ft.Text("Settings"),
                ),
            ],
            on_change=lambda e: print("Selected destination:", e.control.selected_index),
        )
    def main_page_view(self):
        self.page.add(self.rail)
        self.page.update()
class Navigation(UserControl):
    def __init__(self,page: ft.Page):
        super().__init__()
        self.page = page
        self.page.on_route_change = self.route_change
        self.appbar = ft.AppBar(
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
        self.page.appbar = self.appbar
        self.page.update()
    def build(self):
        self.box = Layout(self,self.page)
        return self.box
    def initialize(self):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/",
                [self.appbar, self.box],
            )
        )
        self.page.go("/")
        # self.page.update()
    def route_change(self, e):
        troute = TemplateRoute(self.page.route)
        if troute.match("/"):
            self.box.main_page_view()

        self.page.update()
def main(page: ft.Page):
    page.title = 'LAND расписание'
    app = Navigation(page)
    page.add(app)
    page.update()
    app.initialize()




ft.app(target=main)