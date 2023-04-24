# Django_green_hand
菜鸟教程


#命令行执行
#根据app下的migrations目录中的记录，检测当前model层代码是否发生变化？

python manage.py makemigrations green_hand        （如果不指定子应用名，会把所有子应用生成迁移脚本）

#把orm代码转换成sql语句去数据库执行

python manage.py migrate green_hand 
