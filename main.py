from flet import *
import requests

def main(page:Page):

    def _function(e:ControlEvent):
        api_key:str = "ypT3SNa8gRonXoeIjQFMfklrE8CI5Wo8aurrWKyB"

        if user_input.value:
            api_url = 'https://api.api-ninjas.com/v1/validatephone?number={}'.format(user_input.value)

            response = requests.get(api_url, headers={'X-Api-Key': api_key})

            if response.status_code == requests.codes.ok:
                answer = response.json()

                answer_control = Text(value=f"Is_Valid: {answer['is_valid']}")
                country = Text(value=f"Country: {answer['country']}")
                location = Text(value=f"Location: {answer["location"]}")
                text = Text(value=f"Phone Number: {user_input.value}")

                _answer_column.controls.append(answer_control)
                _answer_column.controls.append(country)
                _answer_column.controls.append(location)
                user_input.value = ""

                page.update()

    page.padding = padding.only(top=75)

    user_input:TextField = TextField(hint_text="phone Number add the area code e.g +1", autofocus=True, width=350,helper_text='add area code e.g +1')
    
    _controls = Row(controls=[user_input, IconButton(icon=icons.SEND_ROUNDED, on_click=_function)])

    _answer_column:Column = Column()
    
    page.add(_controls, _answer_column)


app(target=main)