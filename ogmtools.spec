%define name ogmtools
%define version 1.5
%define release %mkrel 3

Summary: OGG media stream tools
Name: %{name}
Version: %{version}
Epoch: 1
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Video
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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog
%_bindir/*
%_mandir/man1/*


