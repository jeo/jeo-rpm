#!/bin/bash

set -x
set -e

arch=`uname -m`
dist=`cat /etc/rpm/macros.dist | grep "%dist" | cut -f 2 -d ' ' | sed 's/^\.//g'`

# set up some variables
pushd `dirname $0`
build_root=`pwd`/rpmbuild
popd 

rpm_build_root=$build_root/BUILDROOT
rpm_build_dir=$rpm_build_root/BUILD

# figure out the version
ver=`cat $build_root/SPECS/jeo.spec | grep "Version:" | sed 's/Version: *//g'`

# grab the sources
pushd $build_root/SOURCES
set +e; rm *; set -e
wget https://github.com/jeo/jeo-cli/releases/download/$ver/jeo-$ver-cli.zip
wget https://github.com/jeo/jeo-cli/releases/download/$ver/gdaljni-1.9.2-${dist}-${arch}.tgz
popd

# clean out the build root
if [ -d $rpm_build_root ]; then
  rm -rf $rpm_build_root/*
fi

pushd ${build_root}/SPECS

rpmbuild --define "_topdir ${build_root}" --buildroot ${rpm_build_root} -bb jeo.spec

popd


