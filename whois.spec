Summary:	Enhanced WHOIS client
Summary(pl):	Rozszerzony klient WHOIS
Summary(ru):	Улучшенный клиент WHOIS
Summary(uk):	Покращений кл╕╓нт WHOIS
Name:		whois
Version:	4.7.5
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://ftp.debian.org/debian/pool/main/w/whois/%{name}_%{version}.tar.gz
# Source0-md5:	c6657a888a20bd5d5915de6ba18599c8
Patch0:		%{name}-Makefile.patch
URL:		http://www.linux.it/~md/software/
BuildRequires:	gettext-devel
BuildRequires:	libidn-devel
BuildRequires:	perl-base
Obsoletes:	inetutils-whois
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a new whois (RFC 954) client rewritten from scratch. It is
derived from and compatible with the usual BSD and RIPE whois(1)
programs. It is intelligent and can automatically select the
appropriate whois server for most queries.

%description -l pl
To jest nowy klient usЁugi whois (RFC 954) napisany caЁkowicie od
nowa. Jest kompatybilny zarСwno z whois z BSD oraz RIPE. Jest
inteligentny i automatycznie dobiera poprawny serwer whois dla
wiЙkszosci zapytaЯ.

%description -l ru
Это написанный с "нуля" клиент (RFC 954), совместимый с whois(1)
программами BSD и RIPE. В большинстве случаев он может автоматически
выбирать правильный whois сервер в зависимости от запроса.

%description -l uk
Це заново написаний кл╕╓нт whois (RFC 954), сум╕сний з whois(1)
програмами BSD та RIPE. В╕н в б╕льшост╕ випадк╕в може автоматично
вибирати правильний whois сервер в залежност╕ в╕д запиту.

%prep
%setup -q
%patch0 -p1

mv -f po/{no,nb}.po
%{__perl} -pi -e 's/no\.mo/nb.mo/' po/Makefile

%build
%{__make} \
	CC="%{__cc}" \
	OPTS="%{rpmcflags}" \
	HAVE_LIBIDN=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

install whois.conf $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README debian/changelog
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/whois.conf
%{_mandir}/man1/*
