%define name cmdftp
%define version 0.9.7
%define release %mkrel 1

Name:		%name
Version:	%version
Release:	%release
Summary:	A command line shell-like ftp client
Source:		http://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.bz2
URL:		http://www.nongnu.org/cmdftp/
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
