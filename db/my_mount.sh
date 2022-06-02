#!/bin/bash
#Using s3provider... Next step: remove s3fs command for kube system. Or leave in for non-Kube.
#s3fs ike-bucket-small /var/s3fs -o use_cache=/tmp/bucket-cache -o passwd_file=${HOME}/.passwd-s3fs -o allow_other
#/usr/sbin/mysqld --daemonize
touch /var/log/mysqld.log
ln -sf /dev/stdout /var/log/mysqld.log 
#ln -sf /dev/stderr /var/log/mysql/log.err
exec "$@"
