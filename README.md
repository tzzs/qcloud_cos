# 腾讯云COS

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