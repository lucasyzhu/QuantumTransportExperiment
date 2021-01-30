**添加新博文的步骤：**

1. Typora写总结；
2. 输出html文件；
3. 使用html_modify.py程序对html文件进行处理，包括：
   - 为页面添加home建，指向我的博客首页；
   - 修改title为head1，而不是与文件名相同；
   - 删除第5行的链接，该链接不影响网页加载效果，但由于网络问题，有时会影响加载时间；
   - 删除文件中的根目录：`http://www.yuexiaokai.com`，flask会自动补全，在本地和云端，根目录是不一样的；
   - 修改其中的图片缩放格式，typora中图片缩放格式为`style="zoom:80%;"`，转成html文件，在chrome中能正常显示，但firefox中缩放失败。所以需要根据图片尺寸，改为`width="100" height="100"`的缩放格式；
   - 图片src改为base64的数据，直接放到html文件中，封装起来，就不需要额外建文件夹来放图片
4. 在index.md文件中添加新博客的链接，输入html文件，用html_modify.py处理；
5. 将处理后的index文件放到templates对应的文件夹中；
6. 执行web_deployment.sh；
   - 使用scp命令上传到服务器中
   - 重启supervisor
7. 完成部署