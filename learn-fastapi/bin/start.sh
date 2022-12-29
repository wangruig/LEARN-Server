#!/bin/bash

count=0
while true
do 
    # 服务是否还存在
    flag=$(ps -ef | grep han/src_new/server.py | grep -v "grep" | awk "{print $2}")
    if [ -z "$flag" ] # 服务不存在
    then 
        echo `date` - '程序已经停止运行，正在重启中！' >/home/wangruiguo/gnn/han/log/restart.log
        nohup python han/src_new/server.py & >han/log/normal.log 2>&1 &
        count=$[ $count + 1 ] # 服务重启失败次数
        if [ $count -eq 5 ] # 服务失败大于5次
        then
            echo `date` - '程序启动存在异常，正在邮件申报中！' >/home/wangruiguo/gnn/han/log/error.log
            #python han/src_new/send_email.py  # 执行发送邮件脚本
            # echo `date` - '程序启动异常邮件已发送，负责人正在加急处理中！'
            #exit 0 # 退出while循环
        fi
    else
        echo `date` - '程序正在运行，无需启动！' 
        count=0 # 重启成功，次数归0
    fi
    sleep 10m
done
