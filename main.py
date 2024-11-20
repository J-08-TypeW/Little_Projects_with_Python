import flet as ft
import aiohttp
import asyncio

#connector=aiohttp.TCPConnector(ssl=False)
pokemon = 0
async def main(page: ft.Page):
    page.window_width = 720
    page.window_height = 800
    page.window_resizable = True
    page.padding = 0
    page.fonts = {
        "zpix": "https://github.com/SolidZORO/zpix-pixel-font/releases/download/v3.1.8/zpix.ttf"
    }
    page.theme = ft.Theme(font_family="zpix")
    async def petitions(url):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.get(url) as response:
                return await response.json()
            
    async def event1(e: ft.ContainerTapEvent):
        global pokemon
        if e.control == up_arrow:
            pokemon += 1
        else:
            pokemon -= 1
            
        s = (pokemon%150)+1
        resultado = await petitions(f"https://pokeapi.co/api/v2/pokemon/{s}")
        data_shown = f"Name: {resultado['name']}\n\nAbilities:"
        for element in resultado['abilities']:
            abiliti = element['ability']['name']
            data_shown += f"\n{abiliti}"
        data_shown += f"n\nHeight: {resultado['height']}"
        
        texto.value = data_shown
        unspoke_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{s}.png"
        picture.src = unspoke_url
        await page.update_async()
        
    async def light():
        while True:
            await asyncio.sleep(1)
            luz.bgcolor = ft.colors.RED_200
            await page.update_async()
            await asyncio.sleep(0.1)
            luz.bgcolor = ft.colors.RED
            await page.update_async()
    
    luz = ft.Container(width=80, height=80, bgcolor=ft.colors.RED, border_radius=50)
    boton1 = ft.Stack([
        ft.Container(width=80, height=80, bgcolor=ft.colors.WHITE, border_radius=50),
        luz
    ])
    
    items_superior = [
        ft.Container(boton1, width=80, height=80),
        ft.Container(width=40, height=40, bgcolor=ft.colors.RED_300, border_radius=50),
        ft.Container(width=40, height=40, bgcolor=ft.colors.YELLOW, border_radius=50),
        ft.Container(width=40, height=40, bgcolor=ft.colors.GREEN, border_radius=50)
    ]

    unspoke_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/0.png"
    picture = ft.Image(
            src= unspoke_url,
            scale = 10,
            width = 30,
            height = 30,
            top = 135,
            right = 280
        )
    stack_central = ft.Stack([
        ft.Container(width=600, height=300, bgcolor=ft.colors.WHITE, border_radius=20),
        ft.Container(width=570, height=270, bgcolor=ft.colors.BLACK, top=15, left=15),
        picture
    ])
    
    # 180 = pi = 3.14159
    rotation = 3.14159
    triangle = ft.canvas.Canvas([
        ft.canvas.Path([
            ft.canvas.Path.MoveTo(40,0),
            ft.canvas.Path.LineTo(0,50),
            ft.canvas.Path.LineTo(80,50)
        ], 
                       paint=ft.Paint(
                           style=ft.PaintingStyle.FILL,
                       ))
    ], 
                                width=80,
                                height=50)
    
    up_arrow = ft.Container(triangle, width=80, height=50, on_click=event1)
    arrows = ft.Column([
        up_arrow, 
        ft.Container(triangle, rotate=ft.Rotate(angle=rotation), width=80, height=50, on_click=event1)
    ])
    
    texto = ft.Text(
        value = "...",
        color=ft.colors.BLACK, 
        size = 22
    )
    inferior = [
        ft.Container(width=50, ),
        ft.Container(texto, padding=10, width=400, height=300, bgcolor=ft.colors.GREEN_200, border_radius=20),
        ft.Container(arrows, width=80, height=120),
        ft.Container(width=30, )
    ]
    
    superior = ft.Container(content=ft.Row(items_superior), width=600, height=80, margin=ft.margin.only(top=40))
    centro = ft.Container(content=stack_central, width=600, height=300, margin=ft.margin.only(top=40), alignment=ft.alignment.center)
    inferior = ft.Container(content=ft.Row(inferior), width=600, height=300, margin=ft.margin.only(top=40))
    col = ft.Column(spacing=0, controls=[
        superior,
        centro,
        inferior
    ])
    contenedor = ft.Container(col, width=720, height=1280, bgcolor=ft.colors.BLUE, alignment=ft.alignment.top_center)
    
    
    await page.add_async(contenedor)
    await light()

ft.app(target=main)