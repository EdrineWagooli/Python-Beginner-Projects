import flet as ft

def main(page: ft.Page):
    page.title = "Flet Calculator"
    page.window_width = 370  # type: ignore[attr-defined]
    page.window_height = 450  # type: ignore[attr-defined]
    page.theme_mode = ft.ThemeMode.DARK

    result = ft.Text(value="0", size=32, color=ft.Colors.WHITE)


    # --- Button click function
    def button_click(e):
        data = e.control.data
        current = result.value

        if data == "C":
            result.value = "0"
        elif data == "=":
            try:
                result.value = str(eval(current))
            except Exception:
                result.value = "Error"
        else:
            if current == "0":
                result.value = data
            else:
                result.value = current + data 
        page.update()


    # ---Button helper function
    def btn(label, bgcolor=None):
        return ft.ElevatedButton(
            label,
            data=label,
            on_click=button_click,
            expand=True,
            bgcolor=bgcolor,
        )
        
    page.add(
        ft.Container(
            content=result,
            alignment=ft.Alignment.CENTER_RIGHT,
            padding=20,
            bgcolor=ft.Colors.BLACK
        ),
        ft.Row([btn("7"), btn("8"), btn("9"), btn("/")]),
        ft.Row([btn("4"), btn("5"), btn("6"), btn("*")]),
        ft.Row([btn("1"), btn("2"), btn("3"), btn("-")]),
        ft.Row([btn("C", bgcolor=ft.Colors.RED), btn("0"), btn("=", bgcolor=ft.Colors.GREEN), btn("+")]),
    )

ft.run(main)
        