%define	name	mikmod
%define	version	3.2.1
%define	release	%mkrel 7

Name:		%{name}
Summary:	A MOD music file player
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Sound 
Source0:	%{name}-%{version}.tar.bz2
#Patch0:	mikmod-3.1.6-a-va_end-fixes.patch.bz2
Patch1:		mikmod-3.2.1-fix-warnings.patch
Patch2:		mikmod-3.2.1-document-color-in-man-page.patch
Patch3:		mikmod-3.2.1-playmode-in-man-page.patch
Patch4:		mikmod-3.2.1-fix-hyphen-in-man-page.patch
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
%setup -q
#%patch0 -p1 -b .va_end-fixes
%patch1 -p1 -b .fix_warnings
%patch2 -p1 -b .man_color
%patch3 -p1 -b .man_playmode
%patch4 -p1 -b .man_hyphen

%build
%configure	--enable-color-interface
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


