# jeo RPM Packaging

This repository contains files needed to package jeo for Redhat based systems.

## Distributions

The following distributions are supported and have been tested.

- RHEL/CentOS 6
- Fedora 21


Other distributions and versions are likely to be supported as well, but not
officially verified this time.

## Package Dependencies

The jeo package doesn't declare any dependencies on other packages despite 
having a few runtime dependencies. This is done intentionally to make the 
package as portable as possible since the following dependencies tend to vary
greatly across systems. 

### Java

A 1.8+ java runtime is a hard requirement. Some distributions provide a 1.8 jdk 
out of the box. If not one can be downloaded from 
[Oracle](http://www.oracle.com/technetwork/java/javase/downloads/index.html).

### GDAL

The jeo package ships with built versions of the GDAL java bindings. The gdal 
and ogr based drivers will cease to function without libgdal installed on the 
system. The package manager will warn on install if said libraries are not 
installed. 

See the [GDAL](http://trac.osgeo.org/gdal/wiki/DownloadingGdalBinaries) binary
page for details on installing GDAL on your platform. 

## Prerequisites

Building the rpm package requires a system with `rpmbuild` installed and 
configured. The [vagrant] directory contains a number of vagrant box 
configurations that make it easy to set up such an environment.

Setting up an environment manually is also straight forward. The following 
packages must be present:

    % yum install rpm-build unzip wget

And a file named `.rpmmacros` must exist in the home directory of the user
performing the build. **Never** build as root. The file should contain the
following contents: 

    %_topdir <path to rpmbuild directory>

## Building

To build the package simply run the `build.sh` command in the root of this 
repository. Upon success the jeo rpm should be located in `rpmbuild/RPMS/` 
under the sub-directory matching the architecture of your system. 

