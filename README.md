# jeo RPM Packaging

## Prerequisites

Before rpm packages can be built a few packages must be installed on the system
where the build is occuring.

    % yum install rpm-build unzip

As well a file named `.rpmmacros` must exist in the home directory of the user
performing the build. **Never** build as root. The file should contain the
following contents: 

    %_topdir <path to rpmbuild directory>

## Building

To build the package simply run the `build.sh` command in the root of this 
repository.

