Summary:	whois client program 
Name:		whois
Version:	4.4.7
Release:	1
Copyright:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source:		http://www.linux.it/~md/software/whois_%{version}.tar.gz
Patch:		whois-Makefile.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a new whois (RFC 954) client rewritten from scratch by me.                   
It is derived from and compatible with the usual BSD and RIPE whois(1)               
programs.                                                                            
It is intelligent and can automatically select the appropriate whois                 
server for most queries.                                                             
                                                                                    
%prep
%setup -q 
%patch -p1

%build
make OPTS="$RPM_OPTS_FLAGS" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,TODO}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
