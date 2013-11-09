#!/bin/bash


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
rm *
wget http://ares.boundlessgeo.com/jeo/release/$ver/jeo-$ver-cli.zip
popd

# clean out the build root
if [ -d $rpm_build_root ]; then
  rm -rf $rpm_build_root/*
fi

pushd ${build_root}/SPECS

rpmbuild --define "_topdir ${build_root}" --buildroot ${rpm_build_root} -bb --target noarch jeo.spec

popd


