# @Time    : 2022/3/23 17:25
# @Author  : jimmy989898
# @Title   :

import configparser

config = configparser.ConfigParser()
config.read('conf.ini')

# blog_inform
blog_url = config['blog_inform']['blog_url']
blog_id = config['blog_inform']['blog_id']
username = config['blog_inform']['username']
password = config['blog_inform']['password']

# public_options
is_public = config['publish_options']['publish']


