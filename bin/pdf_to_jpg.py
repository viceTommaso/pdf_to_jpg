# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import os
import shutil
from pdf2image import convert_from_path


source = ".\\pdf\\"
destination = ".\\jpg\\"
del_pdf = False
mkdir = True


def init_directory(dir_ck, dir_vsby, dir_name):
    """
    check if there are any dirs needed to boot
    :param dir_ck: directory to check if exist
    :param dir_vsby: if directory is visible or not (any str/h)
    :param dir_name: the name to print when crated
    :return: 0
    """
    if str(os.path.exists(dir_ck)) == "False":
        os.mkdir(dir_ck)
        msg = f"""{dir_name} DIRECTORY doesn't exist, just created"""
        if dir_vsby == "h":
            os.system(f"""attrib +h {dir_ck}""")
            msg = msg + " and hidden"
        print(msg)
    return 0


def main():
    """
    main
    :return: 0
    """
    init_directory(source,"", "PDF")
    init_directory(destination,"", "JPG")
    
    for root, dirs, files in os.walk(source):
        for i in files:
            v_file = i.split(".")
            images = convert_from_path(source + i)

            if len(images) > 1 and mkdir == True:
                path = os.path.join(destination, i.replace(" ", "_")[:-4])
                try:
                    os.mkdir(path)
                    for f in range(len(images)):
                        images[f].save(f"""{path}\\{v_file[0].replace(" ", "_")}_pag{(f+1):0{len(str(len(images)))}d}.jpg""", 'JPEG')

                except FileExistsError:
                    err_input = input(f"""Il file pdf "{v_file[0]}" è gia stato convertito, sovrascrivere? (s):   """)
                    if err_input == "s":
                        shutil.rmtree(path)
                        os.mkdir(path)
                        for f in range(len(images)):
                            images[f].save(f"""{path}\\{v_file[0].replace(" ", "_")}_pag{(f+1):0{len(str(len(images)))}d}.jpg""", 'JPEG')
                    else:
                        exit()

            elif len(images) > 1 and mkdir == False:
                if str(os.path.exists(f"""{destination}\\{v_file[0].replace(" ", "_")}_pag{1:0{len(str(len(images)))}d}.jpg""")) == "False":
                    for f in range(len(images)):
                        images[f].save(f"""{destination}\\{v_file[0].replace(" ", "_")}_pag{(f+1):0{len(str(len(images)))}d}.jpg""", 'JPEG')
                else:
                    err_input = input(f"""Il file pdf "{v_file[0]}" è gia stato convertito, sovrascrivere? (s):   """)
                    if err_input == "s":
                        for f in range(len(images)):
                            images[f].save(f"""{destination}\\{v_file[0].replace(" ", "_")}_pag{(f+1):0{len(str(len(images)))}d}.jpg""", 'JPEG')
                    else:
                        exit()

            else:
                if str(os.path.exists(f"""{destination}\\{v_file[0].replace(" ", "_")}.jpg""")) == "True":
                    err_input = input(f"""Il file pdf "{v_file[0]}" è gia stato convertito, sovrascrivere? (s):   """)
                    if err_input == "s":
                        images[0].save(f"""{destination}\\{v_file[0].replace(" ", "_")}.jpg""", 'JPEG')
                    else:
                        exit()
                else:
                    images[0].save(f"""{destination}\\{v_file[0].replace(" ", "_")}.jpg""", 'JPEG')

            if del_pdf:
                os.remove(os.path.join(root, i))

    return 0


if __name__ == "__main__":
    main()
