%define debug_package %{nil}

Summary:	OGG media stream tools
Name:		ogmtools
Epoch:		1
Version:	1.5
Release:	8
License:	GPLv2
Group:		Video
Url:		http://www.bunkus.org/videotools/ogmtools/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(vorbis)

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
%{_bindir}/*
%{_mandir}/man1/*

