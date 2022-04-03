#!/bin/bash
s3fs ike-bucket-small /mnt/my-bucket -o use_cache=/tmp/bucket-cache -o passwd_file=${HOME}/.passwd-s3fs -o allow_other
#/usr/sbin/mysqld --daemonize
touch /var/log/mysqld.log
ln -sf /dev/stdout /var/log/mysqld.log 
#ln -sf /dev/stderr /var/log/mysql/log.err
exec "$@"
