# @Time    : 2022/3/23 14:39
# @Author  : jimmy989898

import xmlrpc.client

import config_param

blog_url = config_param.blog_url.strip()

server = None
try:
    server = xmlrpc.client.ServerProxy(blog_url)
except Exception as e:
    e = str(e)
    if 'unsupported XML-RPC protocol' in e:
        print('请查看config.yaml文件中的blog_url,应该是这个URL地址没设置对')