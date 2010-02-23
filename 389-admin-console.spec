Name: 389-admin-console
Version: 1.1.4
Release: 1
Summary: 389 Admin Server Management Console

Group: Applications/System
License: GPLv2
URL: http://port389.org

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Source: http://port389.org/sources/%{name}-%{version}.tar.bz2
Requires: 389-admin
BuildRequires: ant >= 1.6.2
BuildRequires: ldapjdk
BuildRequires: idm-console-framework
BuildRequires: java-devel >= 1:1.6.0
Provides: fedora-ds-admin-console = %{version}-%{release}
Obsoletes: fedora-ds-admin-console < 1.1.4-1

%description
A Java based remote management console used for Managing 389
Admin Server.  Requires the 389 Console to load and run the
jar files.

%package          doc
Summary:          Web docs for 389 Admin Server Management Console
Group:            Documentation
Requires:         %{name} = %{version}-%{release}

%description      doc
Web docs for 389 Admin Server Management Console

%prep
%setup -q
                                                                                
%build
%{ant} \
    -Dconsole.location=%{_javadir} \
    -Dbuilt.dir=`pwd`/built

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/dirsrv/html/java
install -m644 built/package/389-admin* $RPM_BUILD_ROOT%{_datadir}/dirsrv/html/java
install -d $RPM_BUILD_ROOT%{_datadir}/dirsrv/manual/en/admin/help
install -m644 help/en/*.html $RPM_BUILD_ROOT%{_datadir}/dirsrv/manual/en/admin
install -m644 help/en/tokens.map $RPM_BUILD_ROOT%{_datadir}/dirsrv/manual/en/admin
install -m644 help/en/help/*.html $RPM_BUILD_ROOT%{_datadir}/dirsrv/manual/en/admin/help

# create symlinks
pushd $RPM_BUILD_ROOT%{_datadir}/dirsrv/html/java
ln -s 389-admin-%{version}.jar 389-admin-%{major_version}.jar
ln -s 389-admin-%{version}.jar 389-admin.jar
ln -s 389-admin-%{version}_en.jar 389-admin-%{major_version}_en.jar
ln -s 389-admin-%{version}_en.jar 389-admin_en.jar
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_datadir}/dirsrv/html/java/389-admin-%{version}.jar
%{_datadir}/dirsrv/html/java/389-admin-%{major_version}.jar
%{_datadir}/dirsrv/html/java/389-admin.jar
%{_datadir}/dirsrv/html/java/389-admin-%{version}_en.jar
%{_datadir}/dirsrv/html/java/389-admin-%{major_version}_en.jar
%{_datadir}/dirsrv/html/java/389-admin_en.jar

%files doc
%defattr(-,root,root,-)
%dir %{_datadir}/dirsrv/manual/en/admin
%doc %{_datadir}/dirsrv/manual/en/admin/tokens.map
%doc %{_datadir}/dirsrv/manual/en/admin/*.html
%doc %{_datadir}/dirsrv/manual/en/admin/help/*.html

%changelog
