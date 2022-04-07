# @Time    : 2022/3/23 16:28
# @Author  : jimmy989898
# @Title   : MarkDownFile实体类
# @Des     : 需要保证MarkDown文件与文档中的图片必须在同一个目录下

import os
import re

import config_param
import server_proxy as proxy
import mime


class ImageFile:
    def __init__(self, image_path_ab, image_path_in_md, image_name, image_upload_url = None):
        self.image_path_ab = image_path_ab
        self.image_path_in_md = image_path_in_md
        self.image_name = image_name
        self.image_upload_url = image_upload_url


class MarkDownFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None
        self.file_name = None
        try:
            self.file = open(file_path, encoding='utf-8')
            self.file_name = os.path.basename(self.file.name)
        except FileNotFoundError as e:
            print("markdown文件不存在", e)
            raise e
        self.markdown_text = self.file.read()
        print(f'markdown读取成功: {file_path}')
        self.image_files = self.find_images_in_markdown()  # 文档图片绝对路径, 相对路径
        self.images_count = len(self.image_files)
        print(f'markdown图片读取成功, 共: {self.images_count}张图片')
        self.upload_images()
        print(f'上传图片成功')


    def find_images_in_markdown(self) -> []:
        """
        :return: 获取到markdown文档原图片的绝对路径
        """
        print("尝试获取源文档中的所有图片地址")
        image_files = []
        for image_name in re.findall("!\\[.*?]\\((.*)\\)", self.markdown_text):
            img = ImageFile(image_path_in_md=image_name,
                            image_path_ab=os.path.join(os.path.dirname(self.file_path), image_name),
                            image_name=os.path.basename(image_name))
            image_files.append(img)
        return image_files

    def upload_images(self):
        """
        :return: 上传后的图片路径
        """
        path_temp = ""
        for image in self.image_files:
            # 部分app导出markdown时，图片空格可能会采用url编码
            if image.image_path_ab.__contains__('%20'):
                path_temp = image.image_path_ab.replace('%20', ' ')
            with open(path_temp, 'rb') as f:
                _, image_format = os.path.splitext(os.path.basename(f.name))
                file = {
                    "bits": f.read(),
                    "name": os.path.basename(f.name),
                    "type": mime.mime_mapping[image_format]
                }
                url = proxy.server.metaWeblog.newMediaObject(config_param.blog_id,
                                                             config_param.username,
                                                             config_param.password,
                                                             file)['url']
                image.image_upload_url = url

    def replace_md_img(self):
        for images in self.image_files:
            self.markdown_text = self.markdown_text.replace(images.image_path_in_md, images.image_upload_url)
