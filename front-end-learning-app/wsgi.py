import flet as ft
import flet.web
import main

def create_app():
    return ft.app(
        target=main.main,
        view=ft.WEB_BROWSER,
        web_renderer="html"
    )

app = create_app() 