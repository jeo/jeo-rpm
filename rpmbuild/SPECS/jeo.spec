Name: jeo
Version: 0.5
Release: 1%{?dist}
Summary: Lightweight spatial library for Java. 
Group: Applications/Engineering
License: Apache Software License.
URL: http://jeo.io
Source0: https://github.com/jeo/jeo-cli/releases/download/%{version}/jeo-%{version}-cli.zip
Source1: https://github.com/jeo/jeo-cli/releases/download/%{version}/gdaljni-1.9.2-%{dist}-%{arch}.tgz

Requires: which

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
ext_dir=$lib_dir/ext
doc_dir=$RPM_BUILD_ROOT%{_defaultdocdir}/$name-$ver

rm -rf $bin_dir $lib_dir $doc_dir 
mkdir -p $bin_dir
mkdir -p $lib_dir 
mkdir -p $doc_dir

cp $src_dir/bin/jeo $bin_dir
cp $src_dir/lib/* $lib_dir
cp $src_dir/*.txt $doc_dir
cp -R $src_dir/ext $lib_dir

tar xzvf $RPM_SOURCE_DIR/gdaljni-*.tgz -C $ext_dir

# patch the binary to point to the right lib and ext dirs
sed -i 's#REPO="$BASEDIR"/lib#REPO=/usr/share/jeo#g' $bin_dir/jeo
sed -i 's#\(java.library.path=\)\(.*\)"#\1\$REPO/ext"#g' $bin_dir/jeo

%files
%defattr(-,root,root,-)
%{_bindir}/jeo
%{_datadir}/jeo
%{_defaultdocdir}

%changelog
* Mon Mar 02 2015 Justin Deoliveira <jdeolive@gmail.com> - 0.5
- new upstream release
* Mon Mar 24 2014 Justin Deoliveira <jdeolive@boundlessgeo.com> - 0.3
- new upstream release
* Mon Dec 06 2013 Justin Deoliveira <jdeolive@boundlessgeo.com> - 0.2
- new upstream release
* Mon Nov 11 2013 Justin Deoliveira <jdeolive@boundlessgeo.com> - 0.1
- initial package for version 0.1

