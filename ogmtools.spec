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
