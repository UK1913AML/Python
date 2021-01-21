import os
from create_new_file_class import CreateNewFile
from change_file_name_class import ChangeFileName

def start_file_manager():
    if create_new_file_or_change_file_name == 1:
        print("生成するファイルの個数を入力してください")
        while True:
            try:
                items = int(input("個数: "))
                if items != 0:
                    break
            except:
                pass
        print()

        print("連番を接頭の場合は1、接尾は2を入力してください")
        while True:
            try:
                before_or_after = int(input("1(接頭)、または2(接尾): "))
                if before_or_after == 1:
                    break
                if before_or_after == 2:
                    break
            except:
                pass
        print()

        print("連番の桁数を入力してください")
        print("ゼロパディングが不要な場合は0を入力してください")
        while True:
            try:
                padding = int(input("桁数: "))
                break
            except:
                pass
        print()

        print("任意のファイル名を入力してください(ファイル名に使えない文字は除外されます)")
        while True:
            try:
                string = input("ファイル名: ")
                if string != "":
                    break
            except:
                pass
        exclude = ["\\", "/", "*", "?", "<", ">", "|"]
        string = "".join(list(filter((lambda e: not e in exclude), string)))            
        print()

        print("ファイル名と連番を結合する文字、または記号を入力してください")
        print("不要な場合はエンターキーを押してください")
        join = input("結合する文字、または記号: ")
        exclude = ["\\", "/", "*", "?", "<", ">", "|"]
        join = "".join(list(filter((lambda e: not e in exclude), join)))
        print()

        print("拡張子を入力してください")
        print("1(Python), 2(Jupyter), 3(R), 4(CSV), 5(JSON), 6(XML)\n7(JavaScript), 8(PHP), 9(HTML), 10(CSS)\n11(C), 12(C++), 13(C#), 14(Java), 15(SQL), 16(Visual Basic)")
        while True:
            try:
                extension = int(input("拡張子: "))
                if extension in range(1, len(CreateNewFile.registered)+1):
                    break
            except:
                pass

        create_new_file = CreateNewFile(items, before_or_after, padding, string, join, extension)
        create_new_file.create()

    else:
        print("変更する対象の拡張子を入力してください")
        print("すべてのファイルを変更する場合はエンターキーを押してください")
        print("1(Word), 2(Excel), 3(PowerPoint), 4(PDF)\n5(JPG), 6(PNG)\n7(MP3), 8(MP4)\n9(Python), 10(Jupyter), 11(R), 12(CSV), 13(JSON), 14(XML)\n15(JavaScript), 16(PHP), 17(HTML), 18(CSS)\n19(C), 20(C++), 21(C#), 22(Java), 23(SQL), 24(Visual Basic)")
        while True:
            try:
                target = str(input("拡張子: "))
                if target == "":
                    break
                if int(target) in range(1, len(ChangeFileName.registered)+1):
                    break
            except:
                pass
        print()

        print("連番を接頭の場合は1、接尾は2を入力してください")
        while True:
            try:
                before_or_after = int(input("1(接頭)、または2(接尾): "))
                if before_or_after == 1:
                    break
                if before_or_after == 2:
                    break
            except:
                pass
        print()

        print("連番の桁数を入力してください")
        print("ゼロパディングが不要な場合は0を入力してください")
        while True:
            try:
                padding = int(input("桁数: "))
                break
            except:
                pass
        print()

        print("任意のファイル名を入力してください(ファイル名に使えない文字は除外されます)")
        while True:
            try:
                string = input("ファイル名: ")
                if string != "":
                    break
            except:
                pass
        exclude = ["\\", "/", "*", "?", "<", ">", "|"]
        string = "".join(list(filter((lambda e: not e in exclude), string)))            
        print()

        print("ファイル名と連番を結合する文字、または記号を入力してください")
        print("不要な場合はエンターキーを押してください")
        join = input("結合する文字、または記号: ")
        exclude = ["\\", "/", "*", "?", "<", ">", "|"]
        join = "".join(list(filter((lambda e: not e in exclude), join)))
        print()
        
        print("拡張子を入力してください")
        print("1(Word), 2(Excel), 3(PowerPoint), 4(PDF)\n5(JPG), 6(PNG)\n7(MP3), 8(MP4)\n9(Python), 10(Jupyter), 11(R), 12(CSV), 13(JSON), 14(XML)\n15(JavaScript), 16(PHP), 17(HTML), 18(CSS)\n19(C), 20(C++), 21(C#), 22(Java), 23(SQL), 24(Visual Basic)")
        while True:
            try:
                extension = int(input("拡張子: "))
                if extension in range(1, len(ChangeFileName.registered)+1):
                    break
            except:
                pass

        change_file_name = ChangeFileName(target, before_or_after, padding, string, join, extension)
        change_file_name.target_extension()
        change_file_name.change()


if __name__ == "__main__":
    path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "/Desktop/result"
    try:
        os.makedirs(path)
    except:
        pass
    print("ファイル生成は1、ファイル名変更は2をを入力してください")
    while True:
        try:
            create_new_file_or_change_file_name = int(input("1(ファイル生成)、または2(ファイル名変更): "))
            if create_new_file_or_change_file_name == 1:
                break
            if create_new_file_or_change_file_name == 2:
                break
        except:
            pass
    print()
    start_file_manager()
