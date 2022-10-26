from datetime import datetime
import os
import sys


def name_my_file():
    """
    creates a filename from current date, script name and file extension
    :return: string
    todo: add url endpoint. necessary? markup?
    """
    current_time = datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
    current_script_name = os.path.basename(sys.argv[0])
    file_extension = '.png'

    file_name=current_time+'_'+current_script_name+file_extension

    if __name__ == '__main__':

        print('-----===-----===-----')
        print('Current time:\n    ', current_time)
        print('Current filename:\n    ', current_script_name)
        print('Returned value:\n    ', file_name)
        print('-----===-----===-----')

    return file_name


if __name__ == '__main__':
    name_my_file()