import flet as f

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

    

    layout = f.Container(padding=10)
    # def on_change_col_field(e):
    #     if e.control.value:
    #         b1.disabled = False
    #     else:
    #         b1.disabled = True
    #     page.update()
        
    # def add(e):
    #     if dd.value == None or dd.value == 'New col':
    #         table.columns.append(f.DataColumn(f.Text(f1.value)))
    #         dd.options.append(f.dropdown.Option(f1.value))
            
    #     else:
    #         table.rows.append(
    #             f.DataRow(
    #                 cells=[
    #                     f.DataCell(f.Text(f1.value)),
    #                 ],
    #             ),
    #         )
    #     f1.value = ''
    #     b1.disabled = True
    #     page.update()


    # dd = f.Dropdown(
    #     width=100,
    #     options=[f.dropdown.Option("New col")],
    # )
    # table = f.DataTable()
    # f1 = f.TextField(label="name obj",on_change=on_change_col_field,)
    # b1 = f.FilledButton(text='add obj', on_click=add,disabled=True)
    # page.add(
    #     f.Row(controls=[
    #     dd,
    #     f1,
    #     b1,
    #     ]),
    #     table
    # )
    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    page.add(
        f.ElevatedButton("Open dialog", on_click=open_dlg)
        )


f.app(target=main)