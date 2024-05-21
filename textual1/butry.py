from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll, Vertical
from textual.widgets import Button, Static
from textual.binding import Binding
from textual.widgets import Footer
from textual.widgets import Placeholder



class FooterApp(App):
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),



    ]


class ButtonsApp(App[str]):
    CSS_PATH = "button.tcss"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "HALLO":
            self.notify(
                "Desde el IESS Haría"
                "[b]El 1º del Ciclo superiror[/b]Saluda al mundo",
                title="Saludo negro",
                severity="Warning",
            )



class Intermide(FooterApp,ButtonsApp):

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static("epic message", classes="header"),
            Button("Hallo everynya",id="HALLO"),
        )
        
        yield Footer(

        )
    


if __name__ == "__main__":
    app = Intermide()
    print(app.run())