from datetime import datetime
import os
import sys


def name_my_file():
    """
    creates a filename from current date, script name and extension
    :return: string
    todo: add url endpoint. necessary? markup?
    """
    current_time = datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
    current_script_name = os.path.basename(sys.argv[0])
    file_extension = '.png'

    screenshot_name=current_time+'_'+current_script_name+file_extension

    if __name__ == '__main__':

        print('------------')
        print('current_time from datetime \n', current_time)
        print('current filename\n', current_script_name)
        print('returned value:\n', screenshot_name)
        print('------------')

    return screenshot_name


if __name__ == '__main__':
    name_my_file()