# -*- coding=utf-8
import configparser
import sys
import os

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

# 加载配置信息
config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.dirname(__file__)) + '\\qcloud_cos.ini')
config_qcloud = config['qcloud']

# 设置用户属性, 包括secret_id, secret_key, region
secret_id = config_qcloud['secret_id']
secret_key = config_qcloud['secret_key']
region = 'ap-chongqing'  # 替换为用户的region
token = None  # 使用临时密钥需要传入Token，默认为空,可不填

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token)  # 获取配置对象
client = CosS3Client(config)

bucket = config_qcloud['bucket_name']

# 获取命令行参数
argv = sys.argv[1:]

# 命令行参数检查
if len(argv) == 0:
    print("无文件上传")

# 遍历图片进行上传
for img in argv:
    file_name = config_qcloud['upload_path'] + img.split('/')[-1]
    response = client.upload_file(
        Bucket=bucket,
        LocalFilePath=img,
        Key=file_name,
        PartSize=10,
        MAXThread=10,
        EnableMD5=True
    )
    print(config_qcloud['url'] + file_name)
