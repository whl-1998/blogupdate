# @Time    : 2022/3/23 14:18
# @Author  : jimmy989898

import sys

import file_entity as f
import request_sender as sender


if __name__ == '__main__':
    args = sys.argv
    if not len(args) == 2:
        print("参数中请添加 markdown 文件的绝对路径")
        exit(-1)
    md_file = f.MarkDownFile(file_path=args[1])
    md_file.replace_md_img()
    sender.send_upload_blog_request(md_file)








