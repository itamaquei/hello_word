from flet import *

def main(page:Page):

    def say_something(e:ControlEvent):
        txt.value = "Hello world"
        page.update()

    btn = ElevatedButton("click me", on_click=say_something)
    txt = Text()
    page.add(btn)


app(target=main)