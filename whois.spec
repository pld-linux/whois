Summary:	whois client program 
Summary(pl):	klient us³ugi whois 
Name:		whois
Version:	4.5.11
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source0:	http://www.linux.it/~md/software/%{name}_%{version}.tar.gz
Patch0:		whois-Makefile.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a new whois (RFC 954) client rewritten from scratch by me. It
is derived from and compatible with the usual BSD and RIPE whois(1)
programs. It is intelligent and can automatically select the
appropriate whois server for most queries.

%description -l pl
To jest nowy klient us³ugi whois*RFC 954) napisany ca³kowicie od nowa.
Jest kompatybilny zarówno z whois z BSD oraz RIPE. Jest inteligentny i
automatycznie dobiera poprawny serwer whois dla wiêkszosci zapytañ.

%prep
%setup -q 
%patch -p1

%build
%{__make} OPTS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,TODO}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
