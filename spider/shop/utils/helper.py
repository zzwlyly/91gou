import datetime
import hashlib
import random


def product_code():
    data_code = datetime.datetime.now().strftime('%Y%m%d%H%I%S%f')
    random_code = random.randint(100000, 999999)
    product = data_code + str(random_code)
    return product


def create_fingerprint(url, type="sha1"):
    minst = hashlib.md5() if type == "md5" else hashlib.sha1()
    minst.update(url.encode("utf8"))
    return minst.hexdigest()


def img_replace(url, p):
    str1 = p.search(url)
    if str1:
        return url.replace(str1.group(), 's400x400_jfs')
    else:
        return url.replace('n5', 'n1')


if __name__ == '__main__':
    img = 'https://img14.360buyimg.com/n0/jfs/t18292/6/1262387404/130784/fb52a222/5ac1eae8N1abc7566.jpg'
    url = 'https://img13.360buyimg.com/n7/jfs/t19912/33/927199229/297549/8c269ff0/5b0fca0fN8d5600df.jpg'
    i2 = 'https://img10.360buyimg.com/n5/s54x54_jfs/t18292/6/1262387404/130784/fb52a222/5ac1eae8N1abc7566.jpg'
    print(create_fingerprint(i2))
    # print(product_code())
# 6a1118987b76fad1fd11a13dfc367928086bff67
# 8f1029d705a124004a8d85920b32b1a03114030d
