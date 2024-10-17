Summary:	Userspace file system driver for mounting WebDAV shares
Name:		fusedav
Version:	0.2
Release:	8
Group:		Networking/Other
License:	GPLv2
URL:		https://0pointer.de/lennart/projects/fusedav/
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



%changelog
* Fri Jun 22 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.2-7
+ Revision: 806671
- rebuild for non existent neon virtual provide
- cleaned up spec

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-6mdv2011.0
+ Revision: 618373
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.2-5mdv2010.0
+ Revision: 428971
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.2-4mdv2009.0
+ Revision: 245458
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 0.2-2mdv2008.1
+ Revision: 168417
- fix summary-not-capitalized
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Jul 07 2007 Nicolas Vigier <nvigier@mandriva.com> 0.2-2mdv2008.0
+ Revision: 49360
- add require on fuse

* Wed May 23 2007 Nicolas Vigier <nvigier@mandriva.com> 0.2-1mdv2008.0
+ Revision: 30143
- Import fusedav

