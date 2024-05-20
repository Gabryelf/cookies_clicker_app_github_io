import flet as ft
import requests

# Адрес вашего бота
BOT_URL = "https://t.me/CookiesClickerGameBot/getUserData"

async def main(page: ft.Page) -> None:
    page.bgcolor = "#000000"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {"appetite-italic": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf"}

    page.theme = ft.Theme(font_family="appetite-italic")

    user_id = "<user_id_from_bot>"

    # Отправляем запрос на получение данных пользователя
    response = requests.get(BOT_URL, params={"user_id": user_id})
    if response.status_code == 200:
        data = response.json()
        score = data.get("score")
        energy = data.get("energy")
        # Создаем текстовые элементы с полученными данными
        score_text = ft.Text(value=f"Score: {score}")
        energy_text = ft.Text(value=f"Energy: {energy}")

        container = ft.Container(
            content=ft.Column(controls=[score_text, energy_text], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=ft.colors.WHITE,
            border_radius=10
        )

        stack = ft.Stack(controls=[container])

        page.add(stack)
        await page.update()
    else:
        print("Failed to fetch user data")

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)







if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
