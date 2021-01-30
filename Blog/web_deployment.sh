#将新的Blog项目发送到服务器端
scp -r ../Blog  root@114.116.122.120:Flask

#重启supervisor
ssh root@114.116.122.120 -tt <<EOT
  supervisorctl shutdown
  supervisord -c /etc/supervisor/supervisord.conf
  supervisorctl -c /etc/supervisor/supervisord.conf status app
	exit
EOT

