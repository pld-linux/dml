Summary:	Tool for displaying dialogs from shell
Summary(pl):	Narzędzie do wyświetlania okien dialogowych z shella
Name:		dml
Version:	0.1.2
Release:	1
License:	GPL
Group:		Applications/Terminal
Source0:	ftp://ftp.pld-linux.org/people/malekith/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	64d5f5666b28d06ef2593eae4b363bd7
BuildRequires:	slang-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for displaying dialogs from shell.

%description -l pl
Narzędzie do wyświetlania okien dialogowych z shella.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO NEWS README doc/dml.pl doc/dml.sh
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
