
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (400,600)


class mainLayout(GridLayout):
    expression = ""

    ans = 0
    def update(self):
        self.ids.ex.text = self.expression

    def reset(self):
        self.expression = ""
        self.update()

    def add_char(self, char):
        self.expression += char + ""
        self.update()

    def rm_char(self):

        #self.expression = "".join(self.expression.split().pop())
        temp = list(self.expression)
        try:
            temp.pop()
        except:
            pass
        self.expression = "".join(temp)
        print(self.expression)
        self.update()

    def on_textinput(self):
        self.expression = self.ids.ex.text

    def eval_ex(self):
        self.on_textinput()
        try:
            self.ans1 = str(eval(self.expression))
            ans = self.ans1
            self.ids.res.text = self.ans1


        except:
            self.ids.res.text = "Equation not valid"

class calcApp(App):
    def build(self):
        return mainLayout()




if __name__ == '__main__':
    calcApp().run()
