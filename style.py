import os, time, sys

class bcolors:
    DEFAULT_HEADER = '\033[95m'
    DEFAULT_OKBLUE = '\033[94m'
    DEFAULT_OKCYAN = '\033[96m'
    DEFAULT_OKGREEN = '\033[92m'
    DEFAULT_WARNING = '\033[93m'
    DEFAULT_FAIL = ' \033[91m'
    DEFAULT_ENDC = ' \033[0m'
    RESET = '\u001b[0m'
    COLORS_BLACK = '\u001b[30m'
    COLORS_RED = '\u001b[31m'
    COLORS_GREEN = '\u001b[32m'
    COLORS_YELLOW = '\u001b[33m'
    COLORS_BLUE = '\u001b[34m'
    COLORS_MAGENTA = '\u001b[35m'
    COLORS_CYAN = '\u001b[36m'
    COLORS_WHITE = '\u001b[37m'
    COLORS_BRIGHT_BLACK = '\u001b[30;1m'
    COLORS_BRIGHT_RED = '\u001b[31;1m'
    COLORS_BRIGHT_GREEN = '\u001b[32;1m'
    COLORS_BRIGHT_YELLOW = '\u001b[33;1m'
    COLORS_BRIGHT_BLUE = '\u001b[34;1m'
    COLORS_BRIGHT_MAGENTA = '\u001b[35;1m'
    COLORS_BRIGHT_CYAN = '\u001b[36;1m'
    COLORS_BRIGHT_WHITE = '\u001b[37;1m'
    BACKGROUND_BLACK = '\u001b[40m'
    BACKGROUND_RED = '\u001b[41m'
    BACKGROUND_GREEN = '\u001b[42m'
    BACKGROUND_YELLOW = '\u001b[43m'
    BACKGROUND_BLUE = '\u001b[44m'
    BACKGROUND_MAGENTA = '\u001b[45m'
    BACKGROUND_CYAN = '\u001b[46m'
    BACKGROUND_WHITE = '\u001b[47m'
    BACKGROUND_BRIGHT_BLACK = '\u001b[40;1m'
    BACKGROUND_BRIGHT_RED = '\u001b[41;1m'
    BACKGROUND_BRIGHT_GREEN = '\u001b[42;1m'
    BACKGROUND_BRIGHT_YELLOW = '\u001b[43;1m'
    BACKGROUND_BRIGHT_BLUE = '\u001b[44;1m'
    BACKGROUND_BRIGHT_MAGENTA = '\u001b[45;1m'
    BACKGROUND_BRIGHT_CYAN = '\u001b[46;1m'
    BACKGROUND_BRIGHT_WHITE = '\u001b[47;1m'
    BOLD = '\u001b[1m'
    UNDERLINE = '\u001b[4m'
    REVERSED = '\u001b[7m'
    CLEAN_SCREEN = '\u001b[2J'
    CLEAN_LINE = '\u001b[2K'

def loading():
    print ("Loading...")
    for i in range(0, 100):
        time.sleep(0.1)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print
   
    
