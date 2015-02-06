%define name cmdftp
%define version 0.9.7
%define release 6

Name:		%name
Version:	%version
Release:	%release
Summary:	A command line shell-like ftp client
Source:		http://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.bz2
URL:		http://www.nongnu.org/cmdftp/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Group:		Networking/File transfer
License:	GPL
%description
cmdftp is a command line FTP client for Unix under GPL.

Features include passive mode for all data transfers, shell like
transparent syntax for local and remote modes, multiple and recursive
file transfers using wildcards, recursive copy and move commands, remote
and local text file viewing and editing, network errors detection and
resuming of currently executing command, partial download resuming (if
server accepts REST command), tab completion for both local and remote
names, autologin using classic ~/.netrc approach, large file support.

cmdftp is aimed at being small and simple. 

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall

%clean
%{__rm} -Rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-5mdv2011.0
+ Revision: 617072
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.9.7-4mdv2010.0
+ Revision: 424882
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.9.7-3mdv2009.0
+ Revision: 243559
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.9.7-1mdv2008.1
+ Revision: 136330
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Funda Wang <fwang@mandriva.org> 0.9.7-1mdv2008.0
+ Revision: 76773
- New version 0.9.7

* Thu Jul 19 2007 Funda Wang <fwang@mandriva.org> 0.9.6-1mdv2008.0
+ Revision: 53548
- New version

* Tue Jul 10 2007 Nicolas Vigier <nvigier@mandriva.com> 0.9.5-1mdv2008.0
+ Revision: 51013
- Import cmdftp

