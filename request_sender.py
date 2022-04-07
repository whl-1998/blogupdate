# @Time    : 2022/3/23 17:39
# @Author  : jimmy989898
# @Title   :

from file_entity import MarkDownFile
from server_proxy import server
import config_param as cf


def send_upload_blog_request(md_file: MarkDownFile):
    new_post(md_file.markdown_text, md_file.file_name)
    print(f"markdown上传成功, 博客标题为'{md_file.file_name}', 状态为'未发布', 请到博客园后台查看")


def new_post(description, title, categories=None, is_public=False):
    if categories is None:
        categories = ['[Markdown]']
    post_request = dict(description=description, title=title, categories=categories)
    server.metaWeblog.newPost(cf.blog_id,
                              cf.username,
                              cf.password,
                              post_request,
                              is_public)