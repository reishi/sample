#!/bin/sh
# Usage: sudo sh -ex ./python3-centos70-install.sh

yum install -y readline-devel openssl-devel tcl-devel tk-devel gcc gcc-gfortran gcc-c++ blas-devel lapack-devel libpng-devel ghostscript xorg-x11-xauth

cd /tmp
curl -O https://www.python.org/ftp/python/3.4.1/Python-3.4.1.tgz
tar xzf Python-3.4.1.tgz
cd Python-3.4.1
./configure
make install

cd /tmp
/usr/local/bin/pip3 install numpy scipy scikit-learn matplotlib ipython
