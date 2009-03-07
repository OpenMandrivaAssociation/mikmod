%define	name	mikmod
%define	version	3.2.2
%define prerel beta1
%define	release	%mkrel 0.%prerel.2

Name:		%{name}
Summary:	A MOD music file player
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Sound 
Source0:	%{name}-%{version}-%prerel.tar.gz
#gw from Fedora, fix compiler warnings
Patch: mikmod-3.2.2-beta1-missing-protos.patch
URL:		http://mikmod.raphnet.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libmikmod-devel ncurses-devel

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
%setup -q -n %name-%version-%prerel
%patch -p1 -b .missing-protos

%build
%configure2_5x	--enable-color-interface
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -fr %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%_datadir/%name

