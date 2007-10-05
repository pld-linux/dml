Summary:	Tool for displaying dialogs from shell
Summary(pl.UTF-8):	Narzędzie do wyświetlania okien dialogowych z shella
Name:		dml
Version:	0.1.6
Release:	3
License:	GPL v2
Group:		Applications/Terminal
Source0:	ftp://ftp.pld-linux.org/people/malekith/dml/%{name}-%{version}.tar.gz
# Source0-md5:	1862186f09b0c82fd69c50364fbbd638
Patch0:		%{name}-utf8.patch
Patch1:		%{name}-input_utf8.patch
BuildRequires:	slang-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for displaying dialogs from shell.

%description -l pl.UTF-8
Narzędzie do wyświetlania okien dialogowych z shella.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
