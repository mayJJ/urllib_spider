from baike_spider import html_downloader
from baike_spider import html_outputer
from baike_spider import html_parser
from baike_spider import url_manager



class SpiderMain:
    
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
#         while self.urls.has_new_url():
#             try:
                #注意变量名，urls，不是url,还是太粗心
                #new_url = self.url.get_new_url()
                
        for x in range(100):
            new_url = self.urls.get_new_url() # 添加单个url
            print('craw%d : %s' %(count, new_url))
            html_cont = self.downloader.download(new_url)

 
#                  new_urls, new_data = self.parser.parse(new_url, html_cont)
            new_urls,new_data = self.parser.parser(new_url, html_cont)
            self.urls.add_new_urls(new_urls)  # 添加批量url
            self.outputer.collect_data(new_data)
                
                
                
#                 if count == 10:
#                     break
#              
            count = count+1
#             except:
#                 print("craw failed")
        
#         .output_html()
        self.outputer.output_data()
             



if __name__=="__main__":
    
    # root_url = "http://baike.baidu.com/item/Python"  "
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)


