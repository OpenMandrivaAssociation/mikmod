Name:		mikmod
Summary:	A MOD music file player
Version:	3.2.2
Release:	1
License:	GPLv2+
Group:		Sound 
Source0:	%{name}-%{version}.tar.gz
Patch1:		mikmod-3.2.2-fix-str-fmt.patch
URL:		http://mikmod.raphnet.net/
BuildRequires:	libmikmod-devel pkgconfig(ncurses)

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
%patch1 -p0

%build
%configure2_5x	--enable-color-interface
%make

%install
%makeinstall

%files
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
