Summary:	Enhanced WHOIS client
Summary(pl):	Rozszerzony klient WHOIS
Summary(ru):	���������� ������ WHOIS
Summary(uk):	���������� �̦��� WHOIS
Name:		whois
Version:	4.7.11
Release:	1
License:	GPL
Group:		Networking/Utilities
#Source0:	http://www.linux.it/~md/software/%{name}_%{version}.tar.gz
Source0:	http://ftp.debian.org/debian/pool/main/w/whois/%{name}_%{version}.tar.gz
# Source0-md5:	aca7ac4c907232f2eea5e7cbb7d6245d
URL:		http://www.linux.it/~md/software/
BuildRequires:	gettext-devel
BuildRequires:	libidn-devel
BuildRequires:	%{_bindir}/perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a new whois (RFC 954) client rewritten from scratch. It is
derived from and compatible with the usual BSD and RIPE whois(1)
programs. It is intelligent and can automatically select the
appropriate whois server for most queries.

%description -l pl
To jest nowy klient us�ugi whois (RFC 954) napisany ca�kowicie od
nowa. Jest kompatybilny zar�wno z whois z BSD oraz RIPE. Jest
inteligentny i automatycznie dobiera poprawny serwer whois dla
wi�kszosci zapyta�.

%description -l ru
��� ���������� � "����" ������ (RFC 954), ����������� � whois(1)
����������� BSD � RIPE. � ����������� ������� �� ����� �������������
�������� ���������� whois ������ � ����������� �� �������.

%description -l uk
�� ������ ��������� �̦��� whois (RFC 954), ��ͦ���� � whois(1)
���������� BSD �� RIPE. ��� � ¦�����Ԧ �����˦� ���� �����������
�������� ���������� whois ������ � ��������Ԧ צ� ������.

%prep
%setup -q

mv -f po/{no,nb}.po
%{__perl} -pi -e 's/no\.mo/nb.mo/' po/Makefile

%build
%{__make} \
	CC="%{__cc}" \
	OPTS="%{rpmcflags}" \
	HAVE_LIBIDN=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1}

install whois.conf $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	BASEDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README debian/changelog
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/whois.conf
%{_mandir}/man1/*
