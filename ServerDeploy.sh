#!/usr/bin/bash
# This is designed for MY development boxes, DO NOT expect this to work for you
# Run this as "sudo yes | ./ServerDeploy.sh" unless you hate yourself

# Check if user is root
if [[ $EUID -ne 0 ]] ; then
	echo "Error: This script must be run with root access."
	exit 1
fi

echo -n "Updating your system..."
aptitude update
aptitude upgrade

echo -n "Installing dem utilities..."
aptitude install autoconf build-essentials screen sudo libpcre3-dev libssl-dev libtool libevent-dev psmisc python-dev libxml2 libxml2-dev git-core byobu htop nethogs vnstat gcc
#aptitude install ia32-libs libexpat1-dev

echo -n "Installing Go 1.0.3..."
cd /var/tmp
wget -q https://go.googlecode.com/files/go1.0.3.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.0.3.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin

echo -n "Installing OpenSSL 1.0.1e..."
cd /var/tmp
wget -q http://openssl.org/source/openssl-1.0.1e.tar.gz
tar zxf openssl-*
cd openssl-*
./config --prefix=/usr zlib-dynamic --openssldir=/etc/ssl shared
make
make install

#echo -n "Installing Bind with GeoIP..."
#cd /var/tmp
#wget -q http://geolite.maxmind.com/download/geoip/api/c/GeoIP.tar.gz
#wget -q <url to bind>
#tar xzf GeoIP.tar.gz
#cd GeoIP-*
#./configure --prefix=/usr/local/geoip
#make
#make install
#cd /var/tmp
#tar xzf bind-*
#cd /var/tmp/bind-*
#wget -q <patch to bind-* at https://code.google.com/p/bind-geoip/downloads/list>
#patch -p0 -b < bind-geoip-*.patch
#autoconf
#./configure --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --sysconfdir=/etc/bind --localstatedir=/var --enable-threads --enable-largefile --with-libtool --enable-shared --enable-static --with-openssl=/usr --with-gssapi=/usr --with-gnu-ld --with-dlz-postgres=no --with-dlz-mysql=no --with-dlz-bdb=yes --with-dlz-filesystem=yes --with-dlz-ldap=yes --with-dlz-stub=yes --with-dlz-dlopen=yes --with-geoip=/usr --enable-ipv6 CFLAGS=-fno-strict-aliasing
#make
#make install
#/usr/sbin/update-rc.d -f bind9 defaults

echo -n "Installing PostgreSQL..."
aptitude install postgresql postgresql-client

#echo -n "Installing MySQL Percona Fork 5.5..."
#gpg --keyserver hkp://keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A
#gpg -a --export CD2EFD2A | sudo apt-key add -
#echo "deb http://repo.percona.com/apt squeeze main" >> /etc/apt/sources.list
#echo "deb-src http://repo.percona.com/apt squeeze main" >> /etc/apt/sources.list
#apt-get update
#apt-get install percona-server-server-5.5 percona-server-client-5.5 percona-server-common-5.5 libmysqlclient-dev

echo -n "Installing Python stuff..."
aptitude install python-pip
pip install virtualenv>=1.9 virtualenvwrapper requests

echo -n "Installing uWSGI..."
aptitude install uwsgi

echo -n "Installing Redis..."
aptitude install redis

echo -n "Installing nginx 1.3.10..."
cd /var/tmp
wget https://raw.github.com/oohnoitz/nginx-installer/master/nginx-installer.sh
chmod +x nginx-installer.sh
./nginx-installer.sh 1.3.10

#echo -n "Installing PHP-FPM 5.4.12..."
#apt-get install libbz2-dev libcurl4-dev libxml2-dev libjpeg-dev libpng-dev libtiff-dev libmcrypt-dev locales-all
#cd /var/tmp
#wget -q http://us.php.net/distributions/php-5.4.12.tar.gz
#tar zxf php-*
#cd php-*
#./configure --with-mysql --enable-fpm --enable-zip --enable-sockets --with-pdo-mysql --with-mysqli --with-gettext --with-gd --enable-ftp --enable-exif --with-curl --with-bz2 --with-openssl --with-mcrypt --enable-mbstring --with-jpeg-dir --with-png-dir --with-zlib --enable-bcmath
#make
#make install
#cp sapi/fpm/init.d.php-fpm /etc/init.d/php-fpm
#cp php.ini-production /usr/local/lib/php.ini
#cp /usr/local/etc/php-fpm.conf.default /usr/local/etc/php-fpm.conf
#chmod 755 /etc/init.d/php-fpm
#update-rc.d php-fpm defaults

#echo -q "Installing APC 3.1.13..."
#pecl install APC-3.1.13

#echo -n "Installing SphinxSearch 2.0.6..."
#cd /var/tmp
#wget -q http://sphinxsearch.com/files/sphinx-2.0.5-release.tar.gz
#tar zxf sphinx-*
#cd sphinx-*
#./configure --prefix=/usr/local/sphinx --enable-id64
#make
#make install