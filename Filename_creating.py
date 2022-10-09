from datetime import datetime
import os
import sys


def name_your_file():
    """
    create name from current date and script name
    :return: string
    todo: add url endpoint. necessary? markup?
    """
    current_time = datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
    current_test = os.path.basename(sys.argv[0])

    screenshot_name=current_time+'_'+current_test

    if __name__ == '__main__':

        print('------------')
        print('current_time from datetime \n', current_time)
        print('current filename\n', current_test)
        print('returned value:\n', screenshot_name)
        print('------------')

    return screenshot_name


if __name__ == '__main__':
    name_your_file()