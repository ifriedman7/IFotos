#!/usr/bin/bash
sudo s3fs ike-bucket-small /mnt/my-bucket -o use_cache=/tmp/bucket-cache -o passwd_file=${HOME}/.passwd-s3fs -o ibm_iam_auth -o allow_other
sudo /etc/init.d/mysqld restart