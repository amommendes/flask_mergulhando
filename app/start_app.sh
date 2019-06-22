#Start Flask
echo $(date "+%Y-%m-%d %H:%M:%S") [INFO] Starting Flask

cd /

nohup gunicorn -w 1 -b 0.0.0.0:5000 "app:create_app()" --access-logfile app/guinicorn_access.log --error-logfile app/guinicorn_error.log &

echo $(date "+%Y-%m-%d %H:%M:%S") [INFO] Return code of gunicorn: $?

tail -f  app/guinicorn_*