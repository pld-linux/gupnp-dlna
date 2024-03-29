#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	vala		# Vala binding
%bcond_without	gstreamer	# GStreamer 1.0 metadata backend

Summary:	GUPnP utility library to ease tasks related to DLNA
Summary(pl.UTF-8):	Biblioteka narzędziowa GUPnP ułatwiająca zadania związane z DLNA
Name:		gupnp-dlna
# note: 0.12.x is stable, 0.13.x unstable
Version:	0.12.0
Release:	1
Epoch:		1
License:	LGPL v2+
Group:		Libraries
Source0:	https://download.gnome.org/sources/gupnp-dlna/0.12/%{name}-%{version}.tar.xz
# Source0-md5:	763703ddfa2660ed881296cab5e07047
URL:		https://wiki.gnome.org/Projects/GUPnP
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.38
BuildRequires:	gobject-introspection-devel >= 1.36.0
%if %{with gstreamer}
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
%endif
BuildRequires:	gtk-doc >= 1.11
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 1:2.5.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 2:0.20}
BuildRequires:	xz
Requires:	glib2 >= 1:2.38
Requires:	gstreamer >= 1.0.0
Requires:	gstreamer-plugins-base >= 1.0.0
Requires:	libxml2 >= 1:2.5.0
Obsoletes:	gupnp-dlna-gst-legacy < 0.11
Obsoletes:	gupnp-dlna-gst-legacy-devel < 0.11
Obsoletes:	gupnp-dlna-gst-legacy-static < 0.11
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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 1:2.38
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
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static GUPnP DLNA library.

%description static -l pl.UTF-8
Statyczna biblioteka GUPnP DLNA.

%package apidocs
Summary:	GUPnP DLNA library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki GUPnP DLNA
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
API and internal documentation for GUPnP DLNA library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki GUPnP DLNA.

%package -n vala-gupnp-dlna
Summary:	Vala binding for GUPnP DLNA library
Summary(pl.UTF-8):	Wiązanie języka Vala do biblioteki GUPnP DLNA
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	vala >= 2:0.20
BuildArch:	noarch

%description -n vala-gupnp-dlna
Vala binding for GUPnP DLNA library.

%description -n vala-gupnp-dlna -l pl.UTF-8
Wiązanie języka Vala do biblioteki GUPnP DLNA.

%package gst
Summary:	GStreamer-specific GUPnP-DLNA library
Summary(pl.UTF-8):	Biblioteka GUPnP-DLNA dla GStreamera
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gstreamer >= 1.0.0
Requires:	gstreamer-plugins-base >= 1.0.0

%description gst
GStreamer-specific GUPnP-DLNA library.

%description gst -l devel
Biblioteka GUPnP-DLNA dla GStreamera.

%package gst-devel
Summary:	Header file for GStreamer-specific GUPnP-DLNA library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki GUPnP-DLNA dla GStreamera
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-gst = %{epoch}:%{version}-%{release}
Requires:	gstreamer-devel >= 1.0.0
Requires:	gstreamer-plugins-base-devel >= 1.0.0

%description gst-devel
Header file for GStreamer-specific GUPnP-DLNA library.

%description gst-devel -l pl.UTF-8
Plik nagłówkowy biblioteki GUPnP-DLNA dla GStreamera.

%package gst-static
Summary:	Static GStreamer-specific GUPnP-DLNA library
Summary(pl.UTF-8):	Statyczna biblioteka GUPnP-DLNA dla GStreamera
Group:		Development/Libraries
Requires:	%{name}-gst-devel = %{epoch}:%{version}-%{release}

%description gst-static
Static GStreamer-specific GUPnP-DLNA library.

%description gst-static -l pl.UTF-8
Statyczna biblioteka GUPnP-DLNA dla GStreamera.

%package gst-apidocs
Summary:	GStreamer-specific GUPnP-DLNA library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki GUPnP-DLNA dla GStreamera
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description gst-apidocs
GStreamer-specific GUPnP-DLNA library API documentation.

%description gst-apidocs -l pl.UTF-8
Dokumentacja API biblioteki GUPnP-DLNA dla GStreamera.

%package -n vala-gupnp-dlna-gst
Summary:	Vala binding for GStreamer-specific GUPnP-DLNA library
Summary(pl.UTF-8):	Wiązanie języka Vala do biblioteki GUPnP-DLNA dla GStreamera
Group:		Development/Libraries
Requires:	%{name}-gst-devel = %{epoch}:%{version}-%{release}
Requires:	vala >= 2:0.20
Requires:	vala-gupnp-dlna-gst = %{epoch}:%{version}-%{release}

%description -n vala-gupnp-dlna-gst
Vala binding for GStreamer-specific GUPnP-DLNA library.

%description -n vala-gupnp-dlna-gst -l pl.UTF-8
Wiązanie języka Vala do biblioteki GUPnP-DLNA dla GStreamera.

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
	%{?with_apidocs:--enable-gtk-doc} \
	%{!?with_gstreamer:--disable-gstreamer-metadata-backend} \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# (re)linking fails sometimes on parallel installs
%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_apidocs:%{__rm} -r $RPM_BUILD_ROOT%{_gtkdocdir}}
%{?with_gstreamer:%{__rm} $RPM_BUILD_ROOT%{_libdir}/gupnp-dlna/libgstreamer.la}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgupnp-dlna-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gupnp-dlna-info-2.0
%attr(755,root,root) %{_bindir}/gupnp-dlna-ls-profiles-2.0
%attr(755,root,root) %{_libdir}/libgupnp-dlna-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgupnp-dlna-2.0.so.4
%dir %{_libdir}/gupnp-dlna
%{_libdir}/girepository-1.0/GUPnPDLNA-2.0.typelib
%{_datadir}/gupnp-dlna-2.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgupnp-dlna-2.0.so
%{_datadir}/gir-1.0/GUPnPDLNA-2.0.gir
%dir %{_includedir}/gupnp-dlna-2.0
%dir %{_includedir}/gupnp-dlna-2.0/libgupnp-dlna
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-*information.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-g-values.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-profile*.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-restriction.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-value-list.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-values.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/metadata
%{_pkgconfigdir}/gupnp-dlna-2.0.pc
%{_pkgconfigdir}/gupnp-dlna-metadata-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgupnp-dlna-2.0.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gupnp-dlna
%{_gtkdocdir}/gupnp-dlna-metadata
%endif

%if %{with vala}
%files -n vala-gupnp-dlna
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gupnp-dlna-2.0.deps
%{_datadir}/vala/vapi/gupnp-dlna-2.0.vapi
%endif

%if %{with gstreamer}
%files gst
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgupnp-dlna-gst-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgupnp-dlna-gst-2.0.so.4
%{_libdir}/girepository-1.0/GUPnPDLNAGst-2.0.typelib
%attr(755,root,root) %{_libdir}/gupnp-dlna/libgstreamer.so

%files gst-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgupnp-dlna-gst-2.0.so
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-gst-utils.h
%{_datadir}/gir-1.0/GUPnPDLNAGst-2.0.gir
%{_pkgconfigdir}/gupnp-dlna-gst-2.0.pc

%files gst-static
%defattr(644,root,root,755)
%{_libdir}/libgupnp-dlna-gst-2.0.a

%if %{with apidocs}
%files gst-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gupnp-dlna-gst
%endif

%if %{with vala}
%files -n vala-gupnp-dlna-gst
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gupnp-dlna-gst-2.0.deps
%{_datadir}/vala/vapi/gupnp-dlna-gst-2.0.vapi
%endif
%endif
