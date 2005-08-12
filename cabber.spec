%define		_rc	test1

Summary:	Cabber - console Jabber client
Summary(pl):	Cabber - konsolowy klient Jabbera
Name:		cabber
Version:	0.5.0
Release:	0.%{_rc}.1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-%{_rc}.tar.gz
# Source0-md5:	3c500c721c167a39f5d0d49243a97514
URL:		http://cabber.sourceforge.net/
BuildRequires:	ncurses-ext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cabber is a console Jabber client.

%description -l pl
Cabber to konsolowy klient JAbbera

%prep
%setup -q -n %{name}-%{version}-%{_rc}

%build
rm -f missing

%{__make} \
	 CFLAGS="-I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENT cabberrc.example Changelog README
%attr(755,root,root) %{_bindir}/*
