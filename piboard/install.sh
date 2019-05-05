#!/bin/sh
################################################################################
# This script installs piboard so that it runs at startup
# It must be run as root since it writes to /etc/rc.local
#
# USAGE:
# sudo install.sh
################################################################################

echo Copying rc.local to etc...

sudo cp rc.local /etc/


echo Done.
