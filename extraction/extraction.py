from random_sampling_class import RandomSampling
import os

def start():
    print("\n抽出するファイルの割合、または個数を入力してください")
    while True:
        try:
            value = int(input("割合(%)、または個数: "))
            if value != 0:
                if option == 1:
                    value /= 100
                else:
                    pass
                break
        except:
            pass

    print("\n抽出対象の拡張子を入力してください\n1(Word), 2(Excel), 3(PowerPoint), 4(PDF)\n5(JPG), 6(PNG)\n7(MP3), 8(MP4)\n9(Python), 10(Jupyter), 11(R), 12(CSV), 13(JSON), 14(XML)\n15(JavaScript), 16(PHP), 17(HTML), 18(CSS)\n19(C), 20(C++), 21(C#), 22(Java), 23(SQL), 24(Visual Basic)")
    while True:
        try:
            extension = int(input("拡張子: "))
            if extension in range(1, len(RandomSampling.registered)+1):
                break
        except:
            pass

    random_sampling = RandomSampling(option, value, extension)
    random_sampling.sampling()


if __name__ == "__main__":
    path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "/Desktop/data"
    try:
        os.makedirs(path)
    except:
        pass
    print("抽出方法を入力してください")
    while True:
        try:
            option = int(input("1(割合)、または2(個数): "))
            if option in range(1, 3):
                break
        except:
            pass
    start()
