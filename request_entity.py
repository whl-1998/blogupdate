# @Time    : 2022/3/23 15:41
# @Author  : jimmy989898
# @Title   : metaweblod请求实体
import datetime as datetime
import json
from io import FileIO


class PostRequest:
    def __init__(self,
                 publish_time,
                 description,
                 title,
                 categories=None):
        publish_time = publish_time
        description = description
        title = title
        categories = categories


class MediaObject:
    def __init__(self, blog_id, username, password, file: FileIO):
        self.blog_id = blog_id
        self.username = username
        self.password = password
        self.file = file


m = PostRequest('1', '2', '3')
print(json.dumps(m))
