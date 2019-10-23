import os
import json
from flask import Flask,render_template

app = Flask(__name__)#初始化


class Getfile(object):
    #获取文章存储文件夹路径
    folderpath = os.path.normpath(os.path.join(os.path.dirname(__file__),'..',files))
    def __init__(self):
        self._files = self.filepath()#将文章内容以字典形式存储在变量中

    def filepath(self):
        result = {}
        allfile = os.listdir(self.floderpath)#获取文件夹内所有的文件和文件夹
        for wj in allfile:
            filename = os.path.join(self.floderpath,wj)#遍历文件后得到文件路径
            with open(filename) as f:
                result[filename[:-5]]=json.load(f)#读取文件内容并存入字典 这里是字典嵌套字典
        return result

    def tit(self):
        return [item['title'] for item in self._files.values()]

    def nr(self,wj):
        return self._files.get(wj)

    getfile = Getfile()


@app.route('/')
def index():
    return render_template('index.html',titlist = gitfile.tit())

@app.route('/files/<filename>')
def file(filename):
    files = getfile.nr(filename)
    if ont files:
        abrot(404)
    else:
        retuen render_template('file.html',files = files)


if __name__ = '__main__'
    app.run()
