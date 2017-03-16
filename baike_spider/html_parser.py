'''
url 解析器

'''
from bs4 import BeautifulSoup
import re
import urllib.parse



class HtmlParser(object):

#         获取新的url。 易错点在于：新获取的url都是不完整的，所以要跟页面url拼接。才能找得到页面。
    def get_new_url(self, page_url, soup):
        
        new_urls = set()
        # <a target="_blank" href="/view/592974.htm">解释器</a>  r"/view/\d+.htm"
        links = soup.find_all('a', href=re.compile( r"/view/\d+.htm"))
        for link in links:
#             print(link)
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
            
        
        return new_urls
    
#         获取页面的标题和内容
    def get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        # class是 python 中的关键字，所以记得加上下划线 _
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title")
        res_data['title'] = title_node.get_text()

        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_="lemma-summary" )
        res_data['summary'] = summary_node.get_text()
                 
        return res_data
    
    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
       
        new_url = self.get_new_url(page_url, soup)

        new_data = self.get_new_data(page_url, soup)
        
        return new_url, new_data
    
    



