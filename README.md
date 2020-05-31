# niutrans_client
 使用小牛翻译API的客户端

## apikey
需要在小牛翻译的官网
https://niutrans.com/
申请一个apikey，然后将该apikey写入apikey.txt(注意不要换行)
将apikey.txt放入/usr/bin或当前目录

## sh
```shell script
ts hello
ts "hello world"
ts -z 你好
ts -f zh -t en 你好
ts --auto hello # default use auto
ls | ts -p # use pipe or read from stdin
ts --list 1 # list all supported languages
ts --show hello # more return infos
```