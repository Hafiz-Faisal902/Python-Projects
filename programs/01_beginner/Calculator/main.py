# This file lives right next to Calculator.py, so Python can find it with
# a plain, direct import - no special tricks needed here (unlike the root
# main.py, which has to work around a folder named "01_beginner").
from Calculator import Calculator

# __name__ is a special variable Python sets automatically. Run this file
# directly (`python main.py`) and __name__ becomes "__main__". Import it
# from somewhere else instead, and __name__ becomes the module's name.
# This check means: only start the calculator if this file was launched
# directly, not if something else imported it.
if __name__ == "__main__":
    Calculator()
