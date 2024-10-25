from flet import IconButton, Page, Row, TextField, icons
import flet as ft


def main(page:Page): #funcion pagina
    page.title = "Contador" #nombre pag
    page.vertical_alignment = "center" #ubicacion

    txt_number = TextField(value=0, text_align="right", width= 100) #definimos caja de texto 

    def minus_click(e):
        txt_number.value = int(txt_number.value) - 1 #segun el valor, restar 1
        page.update()
    def plus_click(e):
        txt_number.value = int(txt_number.value) + 1 #segun el valor, sumar 1
        page.update()    
    
    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click), #boton para quitar
                txt_number,
                IconButton(icons.ADD, on_click=plus_click), # boton para añadir


            ],
            alignment="center", #alineamiento
        )
    )

# modo escritorio
ft.app(target=main) #ejecute
