#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	vala		# Vala binding
#
Summary:	GUPnP utility library to ease tasks related to DLNA
Summary(pl.UTF-8):	Biblioteka narzędziowa GUPnP ułatwiająca zadania związane z DLNA
Name:		gupnp-dlna
# note: 0.8.x is stable, 0.9.x unstable
Version:	0.8.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gupnp-dlna/0.8/%{name}-%{version}.tar.xz
# Source0-md5:	84fc9815c13fa7b6cfc15b9d6ce00415
URL:		http://gupnp.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.24
BuildRequires:	gobject-introspection-devel >= 0.6.4
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk-doc >= 1.11
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 1:2.5.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 2:0.18}
%{?with_vala:BuildRequires:	vala-gupnp >= 0.10}
BuildRequires:	xz
# no --disable-vala option; build fails if vala is present, but vala-gupnp is not
%{!?with_vala:BuildConflicts:	vala}
Requires:	glib2 >= 1:2.24
Requires:	gstreamer >= 1.0.0
Requires:	gstreamer-plugins-base >= 1.0.0
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
Requires:	glib2-devel >= 1:2.24
Requires:	gstreamer-devel >= 1.0.0
Requires:	gstreamer-plugins-base-devel >= 1.0.0
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

%package -n vala-gupnp-dlna
Summary:	Vala binding for GUPnP DLNA library
Summary(pl.UTF-8):	Wiązanie języka Vala do biblioteki GUPnP DLNA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.18
Requires:	vala-gupnp >= 0.10

%description -n vala-gupnp-dlna
Vala binding for GUPnP DLNA library.

%description -n vala-gupnp-dlna -l pl.UTF-8
Wiązanie języka Vala do biblioteki GUPnP DLNA.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4
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
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgupnp-dlna-1.1.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gupnp-dlna-info-1.1
%attr(755,root,root) %{_bindir}/gupnp-dlna-ls-profiles-1.1
%attr(755,root,root) %{_libdir}/libgupnp-dlna-1.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgupnp-dlna-1.1.so.3
%{_libdir}/girepository-1.0/GUPnPDLNA-1.1.typelib
%{_datadir}/gupnp-dlna

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgupnp-dlna-1.1.so
%{_datadir}/gir-1.0/GUPnPDLNA-1.1.gir
%{_includedir}/gupnp-dlna-1.1
%{_pkgconfigdir}/gupnp-dlna-1.1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgupnp-dlna-1.1.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gupnp-dlna
%endif

%if %{with vala}
%files -n vala-gupnp-dlna
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gupnp-dlna-1.1.deps
%{_datadir}/vala/vapi/gupnp-dlna-1.1.vapi
%endif
