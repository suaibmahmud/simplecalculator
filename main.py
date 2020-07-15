from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

Window.size = (400, 430)

class CalcGridLayout(GridLayout):

    # for (=) button
    def calculate(self, calculation):
        if calculation:
            try:
                self.d_out.text = str(eval(calculation))
                # this display keyword is linked with .kv file display keyword
                # calculation is a parameter which is sent by TextInput
                # eval('1+1'); output: 2
                # eval() used to evaluate what is sent by TextInput

            except Exception:
                self.d_out.text = 'Syntax ERROR'

    # for (DEL) button
    def del_btn(self, delete):
        self.d_in.text = delete[0:len(delete) - 1]
        # gradually reduce the length of the string by 1 & show in the display

class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()

CalculatorApp().run()
