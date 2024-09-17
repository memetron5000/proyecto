
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\santiago\Desktop\is\aa\build\assets\frame11")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    93.0,
    300.0,
    image=image_image_1
)

canvas.create_text(
    400.0,
    24.0,
    anchor="nw",
    text="BIENVENIDO",
    fill="#000000",
    font=("MicrosoftSansSerif", 32 * -1)
)

canvas.create_text(
    250.0,
    121.0,
    anchor="nw",
    text="Ingrese el ID del envío a ver:",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    631.0,
    135.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=564.0,
    y=118.0,
    width=134.0,
    height=33.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=729.0,
    y=113.0,
    width=50.0,
    height=45.0
)

canvas.create_text(
    273.0,
    173.0,
    anchor="nw",
    text="Datos actuales del envío:",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    272.0,
    213.0,
    anchor="nw",
    text="Guía aérea",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    621.0,
    213.0,
    anchor="nw",
    text="+++",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    274.0,
    253.0,
    anchor="nw",
    text="Cliente:",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    621.0,
    253.0,
    anchor="nw",
    text="+++",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    278.0,
    293.0,
    anchor="nw",
    text="Tipo de medicamento:",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    621.0,
    293.0,
    anchor="nw",
    text="+++",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    274.0,
    333.0,
    anchor="nw",
    text="Destino:",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    621.0,
    335.0,
    anchor="nw",
    text="+++",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    273.0,
    376.0,
    anchor="nw",
    text="Estado:",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    621.0,
    376.0,
    anchor="nw",
    text="+++",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    275.0,
    416.0,
    anchor="nw",
    text="Temperatura:",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    621.0,
    417.0,
    anchor="nw",
    text="+++",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    275.0,
    463.0,
    anchor="nw",
    text="Hora de entrega:",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    621.0,
    456.0,
    anchor="nw",
    text="+++",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    277.0,
    496.0,
    anchor="nw",
    text="Ubicación actual:",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

canvas.create_text(
    621.0,
    496.0,
    anchor="nw",
    text="+++",
    fill="#000000",
    font=("MicrosoftSansSerif", 20 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=13.0,
    y=58.0,
    width=158.0,
    height=56.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=13.0,
    y=149.0,
    width=159.0,
    height=56.0
)
window.resizable(False, False)
window.mainloop()
