Summary:	Tool for displaying dialogs from shell
Summary(pl):	Narzêdzie do wy¶wietlania okien dialogowych z shella
Name:		dml
Version:	0.0.5
Release:	2
License:	GPL
Group:		Applications/Terminal
Group(de):	Applikationen/Terminal
Group(pl):	Aplikacje/Terminal
Source0:	ftp://ftp.pld.org.pl/people/malekith/%{name}-%{version}.tar.gz
BuildRequires:	slang-devel-BOOT
BuildRequires:	uClibc-devel-BOOT
BuildRequires:	slang-devel
#BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	slang

%description
Tool for displaying dialogs from shell.

%description -l pl
Narzêdzie do wy¶wietlania okien dialogowych z shella.

%package BOOT
Summary:	Tool for displaying dialogs from shell - BOOT
Summary(pl):	Narzêdzie do wy¶wietlania okien dialogowych z shella -BOOT
Group:		Applications/Terminal
Group(de):	Applikationen/Terminal
Group(pl):	Aplikacje/Terminal

%description BOOT
Tool for displaying dialogs from shell. Bootdisk version.

%prep
%setup -q

%build
autoheader
automake --add-missing
autoconf 

%configure --disable-nls
%{__make} -C src \
	CFLAGS="-I%{_libdir}/bootdisk%{_includedir} " \
	LDFLAGS="-nostdlib -static -s" \
	LDADD="	%{_libdir}/bootdisk%{_libdir}/libslang.a \
		%{_libdir}/bootdisk%{_libdir}/crt0.o \
		%{_libdir}/bootdisk%{_libdir}/libc.a -lgcc "
mv -f src/dml dml-BOOT

%{__make} distclean
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

install -d $RPM_BUILD_ROOT/usr/lib/bootdisk/bin
install -s dml-BOOT $RPM_BUILD_ROOT/usr/lib/bootdisk/bin/dml

#gzip -9nf AUTHORS TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files BOOT
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/bootdisk/bin/dml
