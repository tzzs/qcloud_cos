# 腾讯云COS

# Status
![Pylint status](https://github.com/tzzs/qcloud_cos/workflows/Pylint/badge.svg)

## upload_for_md

涉及文件
- upload_for_md.py
- qcloud_cos.ini

### qclou_cos.ini 信息配置文件
```ini
[qcloud]
secret_id =              # API密钥 ID
secret_key =             # API密钥 KEY
bucket_name =            # 存储桶名称  样例 cos-xxxxxxxxxx
upload_path =            # 上传地址，可以有多级文件夹  样例  dir1/dir_img/img.png
url =                    # 用于拼接上传后的地址url，可以打开已存在的照片看一下
```

### 调用方法

执行命令，返回图片url

```shell script
> python upload_for_md.py img_path1 img_path2

https://url/img.png
```


### Typora 配置方法

偏好设置 > 图像 > 上传服务设定 > 上传服务:Custom Command > 自定义命令输入以下命令

```shell script
CALL conda.bat activate WEB && python E:/upload_for_md.py
```

> 注：由于我的环境下存在多个python，所以先使用conda激活指定的python环境，然后进行脚本的调用。脚本需要写绝对路径