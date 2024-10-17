Name:		cmdftp
Version:	0.9.8
Release:	2
Summary:	A command line shell-like FTP client
Source:		http://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz
URL:		https://www.nongnu.org/cmdftp/
Group:		Networking/File transfer
License:	GPLv3

%description
cmdftp is a command line FTP client for Unix under GPL.

Features include passive mode for all data transfers, shell like
transparent syntax for local and remote modes, multiple and recursive
file transfers using wild-cards, recursive copy and move commands, remote
and local text file viewing and editing, network errors detection and
resuming of currently executing command, partial download resuming (if
server accepts REST command), tab completion for both local and remote
names, auto-login using classic ~/.netrc approach, large file support.

cmdftp is aimed at being small and simple. 

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

