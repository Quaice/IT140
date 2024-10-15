# /lib/Printer.py

class Printer:
    reset_all = '\033[0m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    reset_text = '\033[39m'
    black_bg = '\033[40m'
    red_bg = '\033[41m'
    green_bg = '\033[42m'
    yellow_bg = '\033[43m'
    blue_bg = '\033[44m'
    magenta_bg = '\033[45m'
    cyan_bg = '\033[46m'
    white_bg = '\033[47m'
    reset_bg = '\033[49m'
    bright = '\033[1m'
    dim = '\033[2m'
    normal = '\033[22m'

    colors = {
        'reset_all': '\033[0m',
        'reset_text': '\033[39m',
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'black_bg': '\033[40m',
        'red_bg': '\033[41m',
        'green_bg': '\033[42m',
        'yellow_bg': '\033[43m',
        'blue_bg': '\033[44m',
        'magenta_bg': '\033[45m',
        'cyan_bg': '\033[46m',
        'white_bg': '\033[47m',
        'reset_bg': '\033[49m',
        'bright': '\033[1m',
        'dim': '\033[2m',
        'normal': '\033[22m',
    }

    checkmark = '\u2714'
    xmark = '\u2716'

    def cprint(self, text):
        if '[_' in text and '[_]' in text:
            output = ''
            instances = text.split('[_]')
            for instance in instances:
                ctag_start = instance.find('[_')
                ctag_end = instance.find('_]')
                ctag = instance[ctag_start:ctag_end + 2]
                color = instance[ctag_start + 2:ctag_end]
                if ctag in instance and color in self.colors:
                    instance = instance.replace(ctag, self.colors[color])
                    instance += self.colors['reset_text']
                output += instance
        else:
            output = text
        return output

    def p(self, text: str,
          fg: str = reset_text,
          bg: str = reset_bg,
          st: str = normal,
          reset: bool = True,
          line: bool = False,
          end: str = '\n'):
        do_reset = self.reset_all if reset else ''
        x = "{}{}{}{}{}".format(fg, bg, st, text, do_reset)
        if line: self.printline()
        print(x, end=end)

    def text_sandwich(self, text: str = '', text_color:str = cyan, char_color: str = yellow, char: str = '#'):
        self.p(char * len(text), char_color)
        self.p("{}".format(text), text_color)
        self.p(char * len(text), char_color)

    def pretty_box(
            self,
            lines: [],
            text_color: str = white,
            box_color: str = white,
            align: str = '^',
            padding: int = 6):
        for (index, line) in enumerate(lines):
            lines[index] = self.cprint(line)
        width = len(max(lines, key=len)) + padding
        # print box header
        self.p('┏', fg=box_color, end='')
        self.p('━' * width, fg=box_color, end='')
        self.p('┓', fg=box_color)
        # print lines of text
        for line in lines:
            line = self.cprint(line)
            pattern = box_color + '┃' + "{:{}{}}" + box_color + '┃'
            self.p(pattern.format(line, align, width))
        # print box footer
        self.p('┗', fg=box_color, end='')
        self.p('━' * width, fg=box_color, end='')
        self.p('┛', fg=box_color)

    def printline(self, width:int = 45, color:str = white, char: str = '-'):
        self.p(char * width, color)