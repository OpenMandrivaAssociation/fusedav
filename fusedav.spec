%define name	fusedav
%define version	0.2
%define release	%mkrel 1

Name:		%name
Version:	%version
Release:	%release
URL:		http://0pointer.de/lennart/projects/fusedav/
License:	GPL
Source:		http://0pointer.de/lennart/projects/fusedav/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
Group:		Networking/Other
Requires:	neon, lynx
BuildRequires:	neon-devel >= 0.26, fuse-devel >= 2.5, lynx, attr-devel
Summary:	fusedav is a Linux userspace file system driver for mounting WebDAV shares
%description
fusedav is a Linux userspace file system driver for mounting WebDAV shares.
It makes use of FUSE as userspace file system API and neon as WebDAV API.

%prep
%setup -q

%build
%configure
make

%install
%makeinstall

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README
%{_bindir}/%{name}
