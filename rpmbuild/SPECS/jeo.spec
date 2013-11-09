Name: jeo
Version: 0.1
Release: 1
Summary: Lightweight spatial library for Java. 
Group: Applications/Engineering
License: Apache Software License.
URL: https://jeo.github.io
Source: http://ares.boundlessgeo.com/${name}/release/%{name}-%{version}-cli.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
BuildRequires: unzip

%description
A library providing low level spatial capabilities with a command line interface.

%prep
%setup -q

%install

name=$RPM_PACKAGE_NAME
ver=$RPM_PACKAGE_VERSION

src_dir=$RPM_BUILD_DIR/$name-$ver
root_dir=$RPM_BUILD_ROOT%{_datadir}/$name
doc_dir=$RPM_BUILD_ROOT%{_defaultdocdir}/$name-$ver

rm -rf $root_dir $doc_dir
mkdir -p $root_dir 
mkdir -p $doc_dir

cp $src_dir/lib/* $root_dir
cp $src_dir/*.txt $doc_dir

%files
%defattr(-,root,root,-)
%{_datadir}/jeo
%{_defaultdocdir}

