# _without_embed - don't build uClibc version
Summary:	Tool for displaying dialogs from shell
Summary(pl):	Narzêdzie do wy¶wietlania okien dialogowych z shella
Name:		dml
Version:	0.0.15
Release:	1
License:	GPL
Group:		Applications/Terminal
Group(de):	Applikationen/Terminal
Group(pl):	Aplikacje/Terminal
Source0:	ftp://ftp.pld.org.pl/people/malekith/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
%if %{!?_without_embed:1}%{?_without_embed:0}
BuildRequires:	slang-devel-embed
BuildRequires:	uClibc-devel
BuildRequires:	uClibc-static
%endif
BuildRequires:	slang-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	slang

%define embed_path	/usr/lib/embed
%define embed_cc	%{_arch}-uclibc-cc
%define embed_cflags	%{rpmcflags} -Os
%define uclibc_prefix	/usr/%{_arch}-linux-uclibc

%description
Tool for displaying dialogs from shell.

%description -l pl
Narzêdzie do wy¶wietlania okien dialogowych z shella.

%package embed
Summary:	Tool for displaying dialogs from shell - BOOT
Summary(pl):	Narzêdzie do wy¶wietlania okien dialogowych z shella -BOOT
Group:		Applications/Terminal
Group(de):	Applikationen/Terminal
Group(pl):	Aplikacje/Terminal

%description embed
Tool for displaying dialogs from shell. Bootdisk version.

%description embed -l pl
Narzêdzie do wy¶wietlania okien dialogowych z shella. Wersja na
bootkietkê.

%prep
%setup -q

%build
autoheader
aclocal
autoconf
automake -a -c

%if %{!?_without_embed:1}%{?_without_embed:0}
%configure --disable-nls
%{__make} -C src \
	CC=%{embed_cc} \
	CFLAGS="%{embed_cflags}" \
	LDADD="-lslang"
mv -f src/dml dml-shared
%{__make} -C src \
	CC=%{embed_cc} \
	CFLAGS="%{embed_cflags}" \
	LDFLAGS="-static" \
	LDADD="-lslang"
mv -f src/dml dml-static
%{__make} distclean
%endif

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{!?_without_embed:1}%{?_without_embed:0}
install -d $RPM_BUILD_ROOT%{embed_path}/{shared,static}
install dml-shared $RPM_BUILD_ROOT%{embed_path}/shared/dml
install dml-static $RPM_BUILD_ROOT%{embed_path}/static/dml
%endif

gzip -9nf AUTHORS TODO NEWS README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%if %{!?_without_embed:1}%{?_without_embed:0}
%files embed
%defattr(644,root,root,755)
%attr(755,root,root) %{embed_path}/*/dml
%endif
