from baike_spider import html_downloader
from baike_spider import html_outputer
from baike_spider import html_parser
from baike_spider import url_manager



class SpiderMain:

#     这里定义SpiderMain类的一些属性。这样就可以创建对象后直接调用。     
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

#       正式的craw爬取主函数。

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
#         把根url添加到new_url列表，这应该没什么问题。
                
        for x in range(1000):
#             1000随意改。不过单线程比较慢。之后会讲解异步爬取和多线程的。
            try:
                new_url = self.urls.get_new_url() # 添加单个url
                print('craw%d : %s' %(count, new_url))
                html_cont = self.downloader.download(new_url)


                new_urls,new_data = self.parser.parser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)  # 添加批量url
                self.outputer.collect_data(new_data)
                
            except AttributeError:
                print('here is a bug, jump')


            count = count+1

 self.outputer.output_data()


# 主程序的入口。 只要是看到 if __name__ =="__mian__": , 就是整个程序从这里开始的地方。在这里调用各种方法。
if __name__=="__main__":
    
    # root_url = "http://baike.baidu.com/item/Python"  "
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)


