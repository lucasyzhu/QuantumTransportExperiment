#讲服务器端的记录文件复制到本地，并覆盖原有的文件
scp   ubuntu@101.32.204.72:Blog/Blog/record.txt .

#将新的Blog项目发送到服务器端
scp -r ../Blog  ubuntu@101.32.204.72:Blog

#重启supervisor
ssh ubuntu@101.32.204.72 -tt <<EOT
  sudo su
  supervisorctl shutdown
  supervisord   -c /etc/supervisor/supervisord.conf
  supervisorctl -c /etc/supervisor/supervisord.conf status Blog
	exit
	exit
EOT

