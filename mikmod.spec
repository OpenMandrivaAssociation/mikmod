%define	name	mikmod
%define	version	3.2.2
%define prerel beta1
%define	release	%mkrel 1.%prerel.6

Name:		%{name}
Summary:	A MOD music file player
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Sound 
Source0:	%{name}-%{version}-%prerel.tar.gz
#gw P0 from Fedora, fix compiler warnings
Patch0:		mikmod-3.2.2-beta1-missing-protos.patch
Patch1:		mikmod-3.2.2-fix-str-fmt.patch
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
%patch0 -p1 -b .missing-protos
%patch1 -p0

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



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.2.2-0.beta1.6mdv2011.0
+ Revision: 666425
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.2-0.beta1.5mdv2011.0
+ Revision: 606643
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.2-0.beta1.4mdv2010.1
+ Revision: 523310
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.2.2-0.beta1.3mdv2010.0
+ Revision: 426118
- rebuild

* Sun Mar 08 2009 Emmanuel Andry <eandry@mandriva.org> 3.2.2-0.beta1.2mdv2009.1
+ Revision: 352766
- diff p1 to fix string format not literal

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Thu Aug 14 2008 Götz Waschk <waschk@mandriva.org> 3.2.2-0.beta1.1mdv2009.0
+ Revision: 271753
- last version
- drop all patches
- patch from fedora to fix compiler warnings
- update license

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 3.2.1-7mdv2009.0
+ Revision: 223260
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 3.2.1-6mdv2008.1
+ Revision: 129945
- kill re-definition of %%buildroot on Pixel's request


* Fri Mar 02 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 3.2.1-6mdv2007.0
+ Revision: 131570
- remove rather useless and conflicting provides/obsoletes
- Import mikmod

* Tue Sep 19 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 3.2.1-4mdv2007.0
- Rebuild

* Tue Jun 06 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 3.2.1-3mdv2007.0
- %%mkrel
- fix summary-ended-with-dot
- drop COPYING as it's license is included in common-licenses
- drop INSTALL as it's of no use
- from debian:
	o Eliminate some compile warnings (P1)
	o Document --color in the manpage (P2)
	o Fix playmode documentation in the manpage. The default: output of
	  mikmod -h does depend on your actual mikmod configuration, and is correct
	  for an unconfigured mikmod
	o Fix manpage to use HYPHEN-MINUS ("\-") instead of HYPHEN ("-"), which
	  would be rendered differently on unicode terminals

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 3.2.1-2mdk
- Rebuild

