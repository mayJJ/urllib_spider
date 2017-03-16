'''
url输出器

'''

# 在这里, 熟悉html基本标签.看完文档,多观察几个页面去.
import os


class HtmlOutputer(object):

    
    def __init__(self):
        self.datas = []
    
    def collect_data(self, data):
        if data is None:
            return None
        
        self.datas.append(data)
        
    def output_data(self):
        
#         fout = ('output.html', 'w')

        #open文件的时候直接指定encoding='utf-8'
        #这里要注意的是乱码的问题，有几个地方的编解码都要一致才不会乱码
        #一个是从服务器获取数据的时候服务器返回数据时的编码
        #第二个是数据在被写入文件的时候的编码
        #第三个是浏览器在读取html文件时的编码（如果不是html文件也是同理，是文件总是要被读取的吧）
        #当遇到编解码不一致时可以在代码里对数据流进行重新编解码
        #两个函数 decode() encode()
        #参数都是编码格式，函数用法就是字面意思
        fout = open('output.html','w',encoding='utf-8')
          
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
         
        for data in self.datas:
            fout.write("<tr>")

            fout.write("<td>%s</td>"  %data['url'])
            fout.write("<td>%s</td>"  %data['title'])
            fout.write("<td>%s</td>"  %data['summary'])
            fout.write("</tr>")
         
         
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        #文件操作完要记得关闭流,不然流一直开着的话很浪费资源，而且对数据很不安全
        #相当于数据流对外是一直暴露着的，也很容易发生异常,内存泄漏什么的
        fout.close




