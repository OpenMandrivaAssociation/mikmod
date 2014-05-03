%define prerel beta1

Summary:	A MOD music file player

Name:		mikmod
Version:	3.3.2
Release:	1
License:	GPLv2+
Group:		Sound 
Url:		http://mikmod.raphnet.net/
Source0:	https://sourceforge.net/projects/mikmod/files/libmikmod/3.3.2/libmikmod-%{version}.tar.gz
#gw P0 from Fedora, fix compiler warnings
Patch0:		mikmod-3.2.2-beta1-missing-protos.patch
Patch1:		mikmod-3.2.2-fix-str-fmt.patch
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
%setup -qn %{name}-%{version}-%{prerel}
%apply_patches

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


