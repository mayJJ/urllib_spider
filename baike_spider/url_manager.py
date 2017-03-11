class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

# 添加一个新的url
    def add_new_url(self, url):
        if url is None:
            return
        
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            
  
# 添加批量的urls    
    def add_new_urls(self, urls):
            
        if urls is None or len(urls)==0:
            return
        for url in urls:
            if url not in self.new_urls and url not in self.old_urls:
                self.new_urls.add(url)
            

# 查看容器中是否有新的url    
    def has_new_url(self):
        return len(self.new_urls) != 0

# 从容器中获取一个新的url    
    def get_new_url(self):
        if self.new_urls.__len__()!=0:
            
            new_url = self.new_urls.pop()  # pop可以从从这个列表获取这个URL，并且移除它
            self.old_urls.add(new_url) 
            return new_url
        print("new_urls 为空")
    
    
        




