'''
url 下载器

'''
import urllib

# 定义一个html的下载器
class HtmlDownloader(object):

#     定义下载方法。传入要下载的页面的url参数。
#     如果 url 为空 ， 返回None
#     如果返回的状态码不等于200， 返回空。 请自行搜索http状态码。了解最基本的1XX, 2XX, 3XX, 4XX, 5XX 最基本的开头的意义
    def download(self,url):
        if url is None:    
            return None
        
        response = urllib.request.urlopen(url)
        
        if response.getcode() != 200:
            return None
        
        return response.read()
            
            
            
        





