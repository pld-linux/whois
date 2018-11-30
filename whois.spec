Summary:	Enhanced WHOIS client
Summary(pl.UTF-8):	Rozszerzony klient WHOIS
Summary(ru.UTF-8):	Улучшенный клиент WHOIS
Summary(uk.UTF-8):	Покращений клієнт WHOIS
Name:		whois
Version:	5.4.0
Release:	1
License:	GPL v2+
Group:		Networking/Utilities
Source0:	http://ftp.debian.org/debian/pool/main/w/whois/%{name}_%{version}.tar.xz
# Source0-md5:	90b97c2431d3fcfc48041264a8c5c6cf
Patch0:		%{name}-idn.patch
Patch1:		%{name}-config.patch
Patch2:		%{name}-mkpwdhash.patch
Patch3:		%{name}-pl.po-update.patch
URL:		https://github.com/rfc1036/whois
BuildRequires:	gettext-tools
BuildRequires:	libidn2-devel >= 2.0.3
BuildRequires:	libxcrypt-devel >= 4.1
BuildRequires:	perl-base
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libidn2 >= 2.0.3
Obsoletes:	inetutils-whois
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a new whois (RFC 954) client rewritten from scratch. It is
derived from and compatible with the usual BSD and RIPE whois(1)
programs. It is intelligent and can automatically select the
appropriate whois server for most queries.

%description -l pl.UTF-8
To jest nowy klient usługi whois (RFC 954) napisany całkowicie od
nowa. Jest kompatybilny zarówno z whois z BSD oraz RIPE. Jest
inteligentny i automatycznie dobiera poprawny serwer whois dla
większosci zapytań.

%description -l ru.UTF-8
Это написанный с "нуля" клиент (RFC 954), совместимый с whois(1)
программами BSD и RIPE. В большинстве случаев он может автоматически
выбирать правильный whois сервер в зависимости от запроса.

%description -l uk.UTF-8
Це заново написаний клієнт whois (RFC 954), сумісний з whois(1)
програмами BSD та RIPE. Він в більшості випадків може автоматично
вибирати правильний whois сервер в залежності від запиту.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Makefile vs po/Makefile mismatch
echo 'install-pos: install' >> po/Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	HAVE_ICONV=1

%{__make} -C po

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1}
%{__make} install install-pos \
	BASEDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

%{__cp} -p whois.conf $RPM_BUILD_ROOT%{_sysconfdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README debian/changelog
%attr(755,root,root) %{_bindir}/mkpwdhash
%attr(755,root,root) %{_bindir}/whois
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/whois.conf
%{_mandir}/man1/mkpwdhash.1*
%{_mandir}/man1/whois.1*
%{_mandir}/man5/whois.conf.5*
