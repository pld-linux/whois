Summary:	whois client program 
Name:		whois
Version:	4.4.4
Release:	1
Copyright:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source:		http://www.linux.it/~md/software/whois_%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This is a new whois (RFC 954) client rewritten from scratch by me.                   
It is derived from and compatible with the usual BSD and RIPE whois(1)               
programs.                                                                            
It is intelligent and can automatically select the appropriate whois                 
server for most queries.                                                             
                                                                                    
%prep
%setup -q 

%build
make \
	OPTS="$RPM_OPTS_FLAGS" \
	LDFLAGS="-s"
	

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -m755 whois  $RPM_BUILD_ROOT%{_bindir}
install whois.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO}.gz

%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
