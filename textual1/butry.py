from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static


class ButtonsApp(App[str]):
    CSS_PATH = "button.tcss"

    def compose(self) -> ComposeResult:
        yield Horizontal(
            VerticalScroll(
                Static("epic message", classes="header"),
                Button("Hallo everynya"),
                Button.error("bye everynya")

            ),

        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.notify(
            "Desde el IESS Haría"
            "[b]El 1º del Ciclo superiror[/b]Saluda al mundo",
            title="Saludo negro",
            severity="Warning",
        )



if __name__ == "__main__":
    app = ButtonsApp()
    print(app.run())