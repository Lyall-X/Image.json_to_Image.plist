# 脚本工具合集

``` 
$ node.js工具(批量修改从网上明文加密的合图)
$ python工具(用正则匹配批量修改内容)
$ 顺手写的README模板(不知道为啥就喜欢搞个模板，可能懒吧)
```

<!--   ![图片加载不出来显示](图片地址) 把图片存到文件夹里，在github打开图片，获取路径 -->

### image_combination
这样的合图![error](https://github.com/1768204470/Image.json_to_Image.plist/blob/master/doc/1.png)

注意：
- 需要类似于[遨游游览器](http://www.maxthon.cn),很好用的浏览器，原理类似于网络传输管理层，所有消息资源发送需要经过它，所以可以存储资源，(图片，视频，音乐......)![error](https://github.com/1768204470/Image.json_to_Image.plist/blob/master/doc/2.png)
- 网页会将图片加密，各种编辑器加密方式不同，也可以自己写方法加密，生成.fui或.json等等
  网上的图片会经过加密，有非明文加密(看不出来的)，要专门解析
  明文加密的(从结构可以直接看出来的):从网站上能获取到png文件和明文加密json文件
- 因为json文件全名是JAVASCRIPT OBJECT NOTATION，所以不需要导入库可以直接操作，其他类型的需要导入fs库
- 思路:用py或node.js写个合图通用处理方法(注意每次新图要改下js里面的内容)，通过读取加密json文件，生成一个plist文件
``` 
$ 获取一个png文件和一个用来解密用的json文件
$ 通过png文件的name得到json文件里的加密方式
$ 将plist文件和png文件放在一个文件夹，用拆图工具拆
```

### image_sequence
``` 
$ 与image_combination相同,裁剪的是序列帧
$ 文件夹里附带两个拆图工具，脚本拆图用Anti_TexturePacker
```

## python工具

两个py demo修改具有重复特性的文件内容
类似[node.js批量修改文件名](https://www.cnblogs.com/wushanbao/p/7003308.html)

## README模板

它只是个readme模板，仅此而已

****
