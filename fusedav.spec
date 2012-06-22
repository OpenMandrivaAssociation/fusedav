Summary:	Userspace file system driver for mounting WebDAV shares
Name:		fusedav
Version:	0.2
Release:	7
Group:		Networking/Other
License:	GPLv2
URL:		http://0pointer.de/lennart/projects/fusedav/
Source0:	http://0pointer.de/lennart/projects/fusedav/%{name}-%{version}.tar.gz
# Patch to fix build on x86_64
# http://ftp.debian.org/debian/pool/main/f/fusedav/fusedav_0.2-1.diff.gz
Patch0:		ne_lfs.dpatch

BuildRequires:	lynx
BuildRequires:	attr-devel
BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(neon)

Requires:	fuse
Requires:	lynx

%description
fusedav is a Linux userspace file system driver for mounting WebDAV shares.
It makes use of FUSE as userspace file system API and neon as WebDAV API.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
%makeinstall

%files
%doc LICENSE README
%{_bindir}/%{name}

