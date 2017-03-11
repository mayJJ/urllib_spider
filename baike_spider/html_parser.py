'''
url 解析器

'''
from bs4 import BeautifulSoup
import re
import urllib.parse



class HtmlParser(object):

        
    def get_new_url(self, page_url, soup):
#         DOM
        
        new_urls = set()
        #   http://baike.baidu.com/item/Python
        # <a target="_blank" href="/view/592974.htm">解释器</a>  r"/view/\d+.htm"
        # "http://user.qzone.qq.com/2297091173/mood"  
        links = soup.find_all('a', href=re.compile( r"/view/\d+.htm"))
        for link in links:
#             print(link)
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
            
        
        return new_urls
    
    def get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        #
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title")
        res_data['title'] = title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        #<a class="c_tx c_tx3 goDetail" title="2016年11月3日 15:10" href="http://user.qzone.qq.com/2297091173/mood/65d4ea88cae21a58f6ec0d00.1">
        summary_node = soup.find('div',class_="lemma-summary" )
        res_data['summary'] = summary_node.get_text()
                 
        return res_data
    
    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        
        #这里的方法名是get_new_url跟get_new_data,没有下划线开头，错误太low、太粗心！
        
#         new_url = self._get_new_url(page_url, soup)
        new_url = self.get_new_url(page_url, soup)
#         new_data = self._get_new_data(page_url, soup)
        new_data = self.get_new_data(page_url, soup)
        
        return new_url, new_data
    
    



