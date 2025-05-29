import flet as ft
import main

def create_app():
    page = ft.Page(
        port=10000,
        view=ft.WEB_BROWSER
    )
    main.main(page)
    return page.web_server

app = create_app() 