%define name	fusedav
%define version	0.2
%define release	%mkrel 4

Name:		%name
Version:	%version
Release:	%release
URL:		http://0pointer.de/lennart/projects/fusedav/
License:	GPL
Source:		http://0pointer.de/lennart/projects/fusedav/%{name}-%{version}.tar.gz
# Patch to fix build on x86_64
# http://ftp.debian.org/debian/pool/main/f/fusedav/fusedav_0.2-1.diff.gz
Patch0:		ne_lfs.dpatch
BuildRoot:	%{_tmppath}/%{name}-root
Group:		Networking/Other
Requires:	neon, lynx, fuse
BuildRequires:	neon-devel >= 0.26, fuse-devel >= 2.5, lynx, attr-devel
Summary:	Userspace file system driver for mounting WebDAV shares
%description
fusedav is a Linux userspace file system driver for mounting WebDAV shares.
It makes use of FUSE as userspace file system API and neon as WebDAV API.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make

%install
%makeinstall

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README
%{_bindir}/%{name}
