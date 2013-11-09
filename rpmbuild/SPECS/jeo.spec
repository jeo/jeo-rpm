Name: jeo
Version: 0.1
Release: 1%{?dist}
Summary: Lightweight spatial library for Java. 
Group: Applications/Engineering
License: Apache Software License.
URL: https://jeo.github.io
Source: http://ares.boundlessgeo.com/${name}/release/%{name}-%{version}-cli.zip

%if 0%{?fedora}
Requires: java-1.7.0-openjdk
%else
Requires: java-1.6.0-openjdk
%endif

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
BuildRequires: unzip, sed

%description
A library providing low level spatial capabilities with a command line interface.

%prep
%setup -q

%install

name=$RPM_PACKAGE_NAME
ver=$RPM_PACKAGE_VERSION

src_dir=$RPM_BUILD_DIR/$name-$ver

bin_dir=$RPM_BUILD_ROOT%{_bindir}
lib_dir=$RPM_BUILD_ROOT%{_datadir}/$name
doc_dir=$RPM_BUILD_ROOT%{_defaultdocdir}/$name-$ver

rm -rf $bin_dir $lib_dir $doc_dir 
mkdir -p $bin_dir
mkdir -p $lib_dir 
mkdir -p $doc_dir

cp $src_dir/bin/jeo $bin_dir
cp $src_dir/lib/* $lib_dir
cp $src_dir/*.txt $doc_dir

# patch the binary to point to the right lib dir
sed -i 's#REPO="$BASEDIR"/lib#REPO=/usr/share/jeo#g' $bin_dir/jeo

%files
%defattr(-,root,root,-)
%{_bindir}/jeo
%{_datadir}/jeo
%{_defaultdocdir}

