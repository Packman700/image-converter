class TextModeSelectMenu:
    def __init__(self):
        self.HR_LEN = 18

    def create_menu(self, title, options_list):
        menu = self._return_menu(title, options_list)

        output = None  # This is chosen option from
        exec_loc = {}
        code = self._return_menu_logic_code(options_list)
        while output is None:
            print(menu)
            exec(code, globals(), exec_loc)
            output = exec_loc["output"]

        return output

    def _return_menu(self, title, options_list):
        spaces = " " * ((self.HR_LEN // 2) - (len(title) // 2))
        formatted_options = list(map(lambda value: value.replace("_", " ").capitalize(), options_list))
        indexes = range(1, len(options_list) + 1)

        menu = "{menu_title}\n{hr}\n{options}".format(
            menu_title=spaces + title.upper(),
            hr="#" * self.HR_LEN,
            options="\n".join(
                map(lambda index, value: "{}. {}".format(index, value),
                    indexes, formatted_options)
            )
        )
        return menu

    @staticmethod
    def _return_menu_logic_code(options_list):
        code = "chosen_option = input('Your chose: ').lower().strip()\n"
        code += "output = None\n"

        for index, option in enumerate(options_list):
            index += 1
            if index == 1:
                code += """if chosen_option in ('{}', '{}', ''):
                                output='{}'\n""".format(option.replace("_", " "), index, option)
            else:
                code += """elif chosen_option in ('{}', '{}'):
                                output='{}'\n""".format(option.replace("_", " "), index, option)
        code += """else:
                    print('Wrong option try again')
                    output=None\n"""

        return code
