from Base.BaseElementEnmu import Element
from Base.BasePickle import *
from Base.BaseFile import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def mk_file():
    destroy()
    mkdir_file(PATH("../Log/"+Element.INFO_FILE))
    mkdir_file(PATH("../Log/"+Element.SUM_FILE))

    data = read(PATH("../Log/"+Element.INFO_FILE))

    data["version"] = "2018.4.28"
    data["sum"] = 0
    data["pass"] = 0
    data["fail"] = 0
    write(data=data, path=PATH("../Log/"+Element.SUM_FILE))





def destroy():
    remove_file(PATH("../Log/"+Element.INFO_FILE))
    remove_file(PATH("../Log/"+Element.SUM_FILE))
    # remove_file(PATH("../Log/"+Element.DEVICES_FILE))


if __name__ == '__main__':
    print(destroy())
    # print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
