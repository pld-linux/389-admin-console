# TODO
# - merge with fedora-ds-console.spec

%define		major_version 1.1
Summary:	389 Admin Server Management Console
Name:		389-admin-console
Version:	1.1.4
Release:	1
License:	GPL v2
Group:		Applications/System
URL:		http://port389.org/
Source0:	http://port389.org/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	55c661be949c27b9ff2f754abbc2607f
BuildRequires:	ant >= 1.6.2
BuildRequires:	idm-console-framework
BuildRequires:	jdk >= 1:1.6.0
BuildRequires:	jpackage-utils
BuildRequires:	ldapsdk
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	389-admin
Provides:	fedora-ds-admin-console = %{version}-%{release}
Obsoletes:	fedora-ds-admin-console < 1.1.4-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Java based remote management console used for Managing 389 Admin
Server. Requires the 389 Console to load and run the jar files.

%package doc
Summary:	Web docs for 389 Admin Server Management Console
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Web docs for 389 Admin Server Management Console

%prep
%setup -q

%build
%ant \
	-Dconsole.location=%{_javadir} \
	-Dbuilt.dir=$(pwd)/built

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/dirsrv/html/java
cp -a built/package/389-admin* $RPM_BUILD_ROOT%{_datadir}/dirsrv/html/java

install -d $RPM_BUILD_ROOT%{_datadir}/dirsrv/manual/en/admin/help
cp -a help/en/*.html $RPM_BUILD_ROOT%{_datadir}/dirsrv/manual/en/admin
cp -a help/en/tokens.map $RPM_BUILD_ROOT%{_datadir}/dirsrv/manual/en/admin
cp -a help/en/help/*.html $RPM_BUILD_ROOT%{_datadir}/dirsrv/manual/en/admin/help

# create symlinks
cd $RPM_BUILD_ROOT%{_datadir}/dirsrv/html/java
ln -s 389-admin-%{version}.jar 389-admin-%{major_version}.jar
ln -s 389-admin-%{version}.jar 389-admin.jar
ln -s 389-admin-%{version}_en.jar 389-admin-%{major_version}_en.jar
ln -s 389-admin-%{version}_en.jar 389-admin_en.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{_datadir}/dirsrv/html/java/389-admin-%{version}.jar
%{_datadir}/dirsrv/html/java/389-admin-%{major_version}.jar
%{_datadir}/dirsrv/html/java/389-admin.jar
%{_datadir}/dirsrv/html/java/389-admin-%{version}_en.jar
%{_datadir}/dirsrv/html/java/389-admin-%{major_version}_en.jar
%{_datadir}/dirsrv/html/java/389-admin_en.jar

%files doc
%defattr(644,root,root,755)
%dir %{_datadir}/dirsrv/manual/en/admin
%{_datadir}/dirsrv/manual/en/admin/tokens.map
%{_datadir}/dirsrv/manual/en/admin/*.html
%{_datadir}/dirsrv/manual/en/admin/help/*.html
