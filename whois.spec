# TODO
# - Why does whois provide something called mkpasswd (also provided by expect)
#   and should we rm it durring %install with a note as to why we aren't using it?
#   - "because of historical reasons" (quoting README)
#
Summary:	Enhanced WHOIS client
Summary(pl.UTF-8):	Rozszerzony klient WHOIS
Summary(ru.UTF-8):	Улучшенный клиент WHOIS
Summary(uk.UTF-8):	Покращений клієнт WHOIS
Name:		whois
Version:	5.0.26
Release:	1
License:	GPL v2+
Group:		Networking/Utilities
Source0:	http://ftp.debian.org/debian/pool/main/w/whois/%{name}_%{version}.tar.xz
# Source0-md5:	236829eea77e85df2443a54815a1b41d
Patch0:		%{name}-idn.patch
Patch1:		%{name}-config.patch
URL:		http://www.linux.it/~md/software/
BuildRequires:	gettext-devel
BuildRequires:	libidn-devel
BuildRequires:	perl-base
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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

mv -f po/{no,nb}.po
%{__perl} -pi -e 's/no\.mo/nb.mo/' po/Makefile

# Makefile vs po/Makefile mismatch
echo 'install-pos: install' >> po/Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	HAVE_LIBIDN=1

%{__make} -C po

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1}

install whois.conf $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install install-pos \
	BASEDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README debian/changelog
%attr(755,root,root) %{_bindir}/whois
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/whois.conf
%{_mandir}/man1/whois.1*
%{_mandir}/man5/whois.conf.5*
