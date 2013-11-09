# jeo RPM Packaging

## Prerequisites

Before rpm packages can be built a few packages must be installed on the system
where the build is occuring.

    % yum install rpm-build unzip wget

If building on a CentOS 5 or RedHat 5 system an additional RPM is needed.
 
    % wget http://buildsys.fedoraproject.org/buildgroups/rhel5/i386/buildsys-macros-5-5.el5.noarch.rpm
    % rpm -iv buildsys-macros-5-5.el5.noarch.rpm

Finally a file named `.rpmmacros` must exist in the home directory of the user
performing the build. **Never** build as root. The file should contain the
following contents: 

    %_topdir <path to rpmbuild directory>

## Building

To build the package simply run the `build.sh` command in the root of this 
repository. Upon success the jeo rpm should be located in `rpmbuild/RPMS/noarch`. 

