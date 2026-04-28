import flet as ft
import requests

def main(page: ft.Page):
    page.title = "BlinkQuick Customer"
    page.theme_mode = "light"
    
    def load_products(e=None):
        # API se data lana
        res = requests.get("http://localhost:8000/get-products").json()
        product_list.controls.clear()
        for p in res:
            product_list.controls.append(
                ft.ListTile(title=ft.Text(p['name']), subtitle=ft.Text(f"₹{p['price']}"))
            )
        page.update()

    product_list = ft.Column()
    
    page.add(
        ft.Text("BlinkQuick: 10 Min Delivery", size=25, weight="bold"),
        ft.ElevatedButton("Refresh Store", on_click=load_products),
        product_list
    )

ft.app(target=main)