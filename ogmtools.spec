%define debug_package %{nil}
%define _disable_ld_no_undefined 1
%define _disable_lto 1

Summary:	OGG media stream tools
Name:		ogmtools
Epoch:		1
Version:	1.5
Release:	21
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
#export CC=gcc
#export CXX=g++
%configure
%make_build

%install
%make_install

%files
%doc README ChangeLog
%{_bindir}/*
%{_mandir}/man1/*
