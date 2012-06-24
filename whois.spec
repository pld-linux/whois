Summary:	Enhanced WHOIS client
Summary(pl):	Rozszerzony klient WHOIS
Summary(ru):	���������� ������ WHOIS
Summary(uk):	���������� �̦��� WHOIS
Name:		whois
Version:	4.6.3
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.linux.it/~md/software/%{name}_%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-pl.po-update.patch
URL:		http://www.linux.it/~md/software/
BuildRequires:	gettext-devel
BuildRequires:	perl
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
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTS="%{rpmcflags} -DHAVE_GETADDRINFO=1"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
