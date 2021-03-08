from create_new_file_class import CreateNewFile
from change_file_name_class import ChangeFileName
import os

def start():
    if option == 1:
        print("\n生成するファイルの個数を入力してください")
        while True:
            try:
                value = int(input("個数: "))
                if value != 0:
                    break
            except:
                pass
    else:
        print("\n変更する対象の拡張子を入力してください\nすべてのファイルを変更する場合はエンターキーを押してください\n1(Word), 2(Excel), 3(PowerPoint), 4(PDF)\n5(JPG), 6(PNG)\n7(MP3), 8(MP4)\n9(Python), 10(Jupyter), 11(R), 12(CSV), 13(JSON), 14(XML)\n15(JavaScript), 16(PHP), 17(HTML), 18(CSS)\n19(C), 20(C++), 21(C#), 22(Java), 23(SQL), 24(Visual Basic)")
        while True:
            try:
                target = str(input("拡張子: "))
                if target == "":
                    break
                if int(target) in range(1, len(ChangeFileName.registered)+1):
                    break
            except:
                pass

    print("\n連番を接頭の場合は1、接尾は2を入力してください")
    while True:
        try:
            position = int(input("1(接頭)、または2(接尾): "))
            if position in range(1, 3):
                break
        except:
            pass

    print("\n連番の桁数を入力してください\nゼロパディングが不要な場合は0を入力してください")
    while True:
        try:
            padding = int(input("桁数: "))
            break
        except:
            pass

    print("\n任意のファイル名を入力してください(ファイル名に使えない文字は除外されます)")
    while True:
        try:
            string = input("ファイル名: ")
            if string != "":
                break
        except:
            pass
    exclude = ["\\", "/", "*", "?", "<", ">", "|"]
    string = "".join(list(filter((lambda e: not e in exclude), string)))            

    print("\nファイル名と連番を結合する文字、または記号を入力してください\n不要な場合はエンターキーを押してください")
    join = input("結合する文字、または記号: ")
    exclude = ["\\", "/", "*", "?", "<", ">", "|"]
    join = "".join(list(filter((lambda e: not e in exclude), join)))

    while True:
        try:
            if option == 1:
                print("\n拡張子を入力してください\n1(Python), 2(Jupyter), 3(R), 4(CSV), 5(JSON), 6(XML)\n7(JavaScript), 8(PHP), 9(HTML), 10(CSS)\n11(C), 12(C++), 13(C#), 14(Java), 15(SQL), 16(Visual Basic)")
            else:
                print("\n拡張子を入力してください\n1(Word), 2(Excel), 3(PowerPoint), 4(PDF)\n5(JPG), 6(PNG)\n7(MP3), 8(MP4)\n9(Python), 10(Jupyter), 11(R), 12(CSV), 13(JSON), 14(XML)\n15(JavaScript), 16(PHP), 17(HTML), 18(CSS)\n19(C), 20(C++), 21(C#), 22(Java), 23(SQL), 24(Visual Basic)")
            extension = int(input("拡張子: "))
            if option == 1:
                if extension in range(1, len(CreateNewFile.registered)+1):
                    break
            else:
                if extension in range(1, len(ChangeFileName.registered)+1):
                    break
        except:
            pass

    if option == 1:
        create_new_file = CreateNewFile(value, position, padding, string, join, extension)
        create_new_file.create()
    else:
        change_file_name = ChangeFileName(target, position, padding, string, join, extension)
        change_file_name.change()


if __name__ == "__main__":
    path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "/Desktop/"
    print("ファイル生成は1、ファイル名変更は2を入力してください")
    while True:
        try:
            option = int(input("1(ファイル生成)、または2(ファイル名変更): "))
            if option in range(1, 3):
                break
        except:
            pass
    try:
        if option == 1:
            os.makedirs(path + "result")
        else:
            os.makedirs(path + "data")
    except:
        pass
    start()
