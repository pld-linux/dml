Summary:	Tool for displaying dialogs from shell
Summary(pl):	Narzędzie do wyświetlania okien dialogowych z shella
Name:		dml
Version:	0.0.15
Release:	2
License:	GPL
Group:		Applications/Terminal
Source0:	ftp://ftp.pld.org.pl/people/malekith/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	slang-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	slang

%description
Tool for displaying dialogs from shell.

%description -l pl
Narzędzie do wyświetlania okien dialogowych z shella.

%prep
%setup -q

%build
autoheader
aclocal
autoconf
automake -a -c

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS TODO NEWS README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
