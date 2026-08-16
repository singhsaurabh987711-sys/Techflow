from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle


class TechFlowApp(App):

    def build(self):

        Window.clearcolor = (0.01, 0.08, 0.02, 1)

        scroll = ScrollView(
            do_scroll_x=False,
            do_scroll_y=True
        )

        main = BoxLayout(
            orientation="vertical",
            padding=[15, 12, 15, 20],
            spacing=12,
            size_hint_y=None
        )

        main.bind(
            minimum_height=main.setter("height")
        )

        # BACKGROUND
        with main.canvas.before:
            Color(0.01, 0.08, 0.02, 1)

            self.bg = Rectangle(
                pos=main.pos,
                size=main.size
            )

        main.bind(
            pos=self.update_bg,
            size=self.update_bg
        )

        # TECHFLOW
        main.add_widget(
            Label(
                text="TECHFLOW",
                font_size=95,
                bold=True,
                color=(0.1, 1, 0.25, 1),
                size_hint_y=None,
                height=125
            )
        )

        # SANDEEP THAKUR
        main.add_widget(
            Label(
                text="SANDEEP THAKUR",
                font_size=65,
                bold=True,
                color=(1, 1, 1, 1),
                size_hint_y=None,
                height=90
            )
        )

        # BUSINESS MANAGEMENT SYSTEM
        main.add_widget(
            Label(
                text="BUSINESS MANAGEMENT SYSTEM",
                font_size=38,
                bold=True,
                color=(0.2, 1, 0.4, 1),
                size_hint_y=None,
                height=65
            )
        )

        # UTTAR PRADESH
        main.add_widget(
            Label(
                text="UTTAR PRADESH",
                font_size=35,
                bold=True,
                color=(0.5, 1, 0.6, 1),
                size_hint_y=None,
                height=55
            )
        )

        # GAP
        main.add_widget(
            Label(
                text="",
                size_hint_y=None,
                height=20
            )
        )

        # SALES
        sales = self.make_button("SALES")
        sales.bind(on_press=self.sales)
        main.add_widget(sales)

        # PROFIT
        profit = self.make_button("PROFIT")
        profit.bind(on_press=self.profit)
        main.add_widget(profit)

        # EXPENSE
        expense = self.make_button("EXPENSE")
        expense.bind(on_press=self.expense)
        main.add_widget(expense)

        # EXIT
        exit_button = self.make_button("EXIT")
        exit_button.bind(on_press=self.stop)
        main.add_widget(exit_button)

        # FOOTER
        main.add_widget(
            Label(
                text="DEVELOPED BY SANDEEP THAKUR",
                font_size=28,
                bold=True,
                color=(0.1, 1, 0.3, 1),
                size_hint_y=None,
                height=60
            )
        )

        scroll.add_widget(main)

        return scroll

    # BACKGROUND
    def update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    # BUTTON DESIGN
    def make_button(self, text):

        return Button(
            text=text,
            font_size=48,
            bold=True,
            color=(0.15, 1, 0.35, 1),
            size_hint_y=None,
            height=100,
            background_normal="",
            background_color=(0.0, 0.04, 0.01, 1)
        )

    # SALES
    def sales(self, instance):

        self.calculator(
            "SALES",
            "Enter Quantity",
            "Enter Price",
            "Sales Amount",
            "multiply"
        )

    # PROFIT
    def profit(self, instance):

        self.calculator(
            "PROFIT",
            "Enter Selling Price",
            "Enter Cost Price",
            "Profit",
            "subtract"
        )

    # EXPENSE
    def expense(self, instance):

        self.calculator(
            "EXPENSE",
            "Enter Expense 1",
            "Enter Expense 2",
            "Total Expense",
            "add"
        )

    # CALCULATOR
    def calculator(
        self,
        title,
        first_hint,
        second_hint,
        result_name,
        operation
    ):

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=18
        )

        first = TextInput(
            hint_text=first_hint,
            input_filter="float",
            multiline=False,
            font_size=30,
            size_hint_y=None,
            height=75
        )

        second = TextInput(
            hint_text=second_hint,
            input_filter="float",
            multiline=False,
            font_size=30,
            size_hint_y=None,
            height=75
        )

        result = Label(
            text=result_name + ": 0",
            font_size=36,
            bold=True
        )

        calculate = Button(
            text="CALCULATE",
            font_size=32,
            bold=True,
            size_hint_y=None,
            height=80
        )

        close = Button(
            text="CLOSE",
            font_size=28,
            bold=True,
            size_hint_y=None,
            height=70
        )

        layout.add_widget(first)
        layout.add_widget(second)
        layout.add_widget(calculate)
        layout.add_widget(result)
        layout.add_widget(close)

        popup = Popup(
            title=title,
            content=layout,
            size_hint=(0.94, 0.80)
        )

        def calculate_result(instance):

            try:

                a = float(first.text)
                b = float(second.text)

                if operation == "multiply":
                    value = a * b

                elif operation == "subtract":
                    value = a - b

                else:
                    value = a + b

                result.text = (
                    result_name
                    + ": "
                    + str(round(value, 2))
                )

            except ValueError:

                result.text = "ENTER VALID NUMBERS"

        calculate.bind(
            on_press=calculate_result
        )

        close.bind(
            on_press=popup.dismiss
        )

        popup.open()


TechFlowApp().run()