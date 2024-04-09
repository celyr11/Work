#Dice Roller (Cely Reyes)
import flet as ft
import random

def main(page: ft.Page):
    def button_clicked(e):
        roll = random.randint(1, 6)
        img.height=160
        img.width=160
        number.value=roll
        if roll == 1: 
            img.src = "https://upload.wikimedia.org/wikipedia/commons/1/1b/Dice-1-b.svg"
        elif roll == 2: 
            img.src = "https://www.svgrepo.com/show/320118/inverted-dice-2.svg"
        elif roll == 3: 
            img.src = "https://www.svgrepo.com/show/320121/inverted-dice-3.svg"
        elif roll == 4: 
            img.src = "https://upload.wikimedia.org/wikipedia/commons/f/fd/Dice-4-b.svg"
        elif roll == 5: 
            img.src = "https://cdn2.iconfinder.com/data/icons/dice-roll/100/dice_5-512.png"
        elif roll == 6: 
            img.src = "https://cdn2.iconfinder.com/data/icons/dice-roll/100/dice_6-512.png"
        page.update()
        
    page.title = "Dice roller"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    img = ft.Image(src="firstface.png", height=160, width=160)
    number = ft.Text(" ")

    page.add(
        img,number, 
        ft.FilledTonalButton(text="Roll Dice",on_click=button_clicked)), 
ft.app(target=main)