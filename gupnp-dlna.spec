#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
#
Summary:	GUPnP utility library to ease tasks related to DLNA
Summary(pl.UTF-8):	Biblioteka narzędziowa GUPnP ułatwiająca zadania związane z DLNA
Name:		gupnp-dlna
# note: 0.6.x is stable, 0.7.x unstable
Version:	0.6.1
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: http://gupnp.org/download
Source0:	http://gupnp.org/sites/all/files/sources/%{name}-%{version}.tar.gz
# Source0-md5:	0265d8864edcddc3367dcfe431c3bb53
URL:		http://gupnp.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gstreamer-devel >= 0.10.29.2
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.32
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.5.0
BuildRequires:	pkgconfig
Requires:	gstreamer >= 0.10.29.2
Requires:	gstreamer-plugins-base >= 0.10.32
Requires:	libxml2 >= 1:2.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUPnP DLNA is a small utility library that aims to ease the tasks
related to DLNA (Digital Living Network Alliance) such as media
profile guessing, transcoding to a given profile, etc.

%description -l pl.UTF-8
GUPnP DLNA to mała biblioteka narzędziowa, której celem jest
ułatwienie wykonywania zadań związanych z DLNA (Digital Living Network
Alliance), takich jak wykrywanie profili multimediów, przekodowywanie
do danego profilu itp.

%package devel
Summary:	Header files for GUPnP DLNA library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GUPnP DLNA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer-devel >= 0.10.29.2
Requires:	gstreamer-plugins-base-devel >= 0.10.32
Requires:	libxml2-devel >= 1:2.5.0

%description devel
Header files for GUPnP DLNA library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GUPnP DLNA.

%package static
Summary:	Static GUPnP DLNA library
Summary(pl.UTF-8):	Statyczna biblioteka GUPnP DLNA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GUPnP DLNA library.

%description static -l pl.UTF-8
Statyczna biblioteka GUPnP DLNA.

%package apidocs
Summary:	GUPnP DLNA library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki GUPnP DLNA
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API and internal documentation for GUPnP DLNA library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki GUPnP DLNA.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_apidocs:--enable-gtk-doc} \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_apidocs:%{__rm} -r $RPM_BUILD_ROOT%{_gtkdocdir}}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgupnp-dlna-1.0.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gupnp-dlna-info
%attr(755,root,root) %{_bindir}/gupnp-dlna-ls-profiles
%attr(755,root,root) %{_libdir}/libgupnp-dlna-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgupnp-dlna-1.0.so.2
%{_datadir}/gupnp-dlna

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgupnp-dlna-1.0.so
%{_includedir}/gupnp-dlna-1.0
%{_pkgconfigdir}/gupnp-dlna-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgupnp-dlna-1.0.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gupnp-dlna
%endif
