# conditional build:
# --without nls
Summary:	Tool for displaying dialogs from shell
Summary(pl):	Narzêdzie do wy¶wietlania okien dialogowych z shella
Name:		dml
Version:	0.0.17
Release:	1
License:	GPL
Group:		Applications/Terminal
Source0:	ftp://ftp.pld.org.pl/people/malekith/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	slang-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for displaying dialogs from shell.

%description -l pl
Narzêdzie do wy¶wietlania okien dialogowych z shella.

%prep
%setup -q

%build
autoheader
aclocal
%{__autoconf}
%{__automake}

%configure %{?_without_nls:--disable-nls}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS TODO NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
