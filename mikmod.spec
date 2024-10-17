Name:		mikmod
Summary:	A MOD music file player
Version:	3.2.8
Release:	6
License:	GPLv2+
Group:		Sound
Source0:	http://sourceforge.net/projects/mikmod/files/mikmod/%{version}/mikmod-%{version}.tar.gz
URL:		https://mikmod.sourceforge.net/
BuildRequires:	libmikmod-devel
BuildRequires:	pkgconfig(ncurses)

%description
MikMod is one of the best and most well known MOD music file players for
UNIX-like systems.  This particular distribution is intended to compile
fairly painlessly in a Linux environment. MikMod uses the OSS /dev/dsp
driver including all recent kernels for output, and will also write .wav
files. Supported file formats include MOD, STM, S3M, MTM, XM, ULT, and IT.
The player uses ncurses for console output and supports transparent
loading from gzip/pkzip/zoo archives and the loading/saving of playlists.

Install the mikmod package if you need a MOD music file player.

%prep
%setup -q
%autopatch -p1

%build
%configure --enable-color-interface
%make

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
