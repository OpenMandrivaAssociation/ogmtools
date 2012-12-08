Summary: OGG media stream tools
Name: ogmtools
Version: 1.5
Epoch: 1
Release: 8
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Video
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libvorbis-devel
BuildRequires: libdvdread-devel
URL: http://www.bunkus.org/videotools/ogmtools/

%description
These tools allow information about (ogminfo) or extraction
from (ogmdemux) or creation of (ogmmerge) OGG media streams.
Note that OGM is used for "OGG media streams".

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README ChangeLog
%_bindir/*
%_mandir/man1/*


%changelog
* Sun Nov 20 2011 Alexander Khrukin <akhrukin@mandriva.org> 1:1.5-8
+ Revision: 732016
- release bump spec file cleaned

* Mon Sep 05 2011 Götz Waschk <waschk@mandriva.org> 1:1.5-7
+ Revision: 698302
- rebuild

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 1:1.5-6mdv2011.0
+ Revision: 278255
- rebuild for new libdvdread

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1:1.5-5mdv2009.0
+ Revision: 254400
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

