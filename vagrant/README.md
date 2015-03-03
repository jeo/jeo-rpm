# Vagrant box for building jeo RPM

This directory contains a [Vagrant](https://www.vagrantup.com/) box configuration for setting up an 
environment capable of building jeo rpm packages. It used [Ansible](http://www.ansible.com/home) to 
provision the box and install the necessary packages and configuration for the rpm build.
environment.

To use this box:

1. Install Vagrant and Ansible
1. Change to this directory and:

        % vagrant up
        % vagrant provision 


By default this box is configured with a recent fedora base box. Update [Vagrantfile](Vagrantfile) 
to change to a different base box and to change other configuration options.