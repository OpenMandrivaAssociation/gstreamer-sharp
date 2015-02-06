%define name gstreamer-sharp
%define version 0.9.2
%define release 5
%define api 0.10

Summary: C#/CLI bindings for GStreamer
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://gstreamer.freedesktop.org/src/%name/%{name}-%{version}.tar.bz2
Patch0: gstreamer-sharp-0.9.2-glib-includes.patch
License: LGPLv2+
Group: System/Libraries
Url: http://gstreamer.freedesktop.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: gtk-sharp2-devel
BuildRequires: libgstreamer-plugins-base-devel >= 0.10.23

%description
There are bindings for the complete GStreamer core and some
of the GStreamer libraries.

%package devel
Group: Development/Other
Summary: C#/CLI bindings for GStreamer - development files
Requires: %name = %version-%release
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description devel
There are bindings for the complete GStreamer core and some
of the GStreamer libraries.

This contains development files needed to build with %{name}.


%package doc
Summary:	Documentation for %name
Group:		Development/Other
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description doc
This package provides API documentation for %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make MONO=mono

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %buildroot%_libdir/lib*a
%if %_lib != lib
mv %buildroot%_libdir/mono %buildroot%_prefix/lib/
%endif

%clean
rm -rf %{buildroot}

%post doc
%_bindir/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi

%files
%defattr(-,root,root)
%doc README AUTHORS TODO
%_libdir/libgstreamersharpglue-%{api}.so
%_prefix/lib/mono/gac/%{name}
%_prefix/lib/mono/%{name}-%{api}

%files doc
%defattr(-,root,root)
%_prefix/lib/monodoc/sources/%{name}-docs.*

%files devel
%defattr(-,root,root)
%_libdir/pkgconfig/%{name}-%{api}.pc
%_datadir/gapi/gstreamer-api.xml


%changelog
* Wed Dec 07 2011 Götz Waschk <waschk@mandriva.org> 0.9.2-4mdv2012.0
+ Revision: 738522
- fix build with new glib
- yearly rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-3mdv2011.0
+ Revision: 610988
- rebuild

* Fri Dec 11 2009 Götz Waschk <waschk@mandriva.org> 0.9.2-2mdv2010.1
+ Revision: 476295
- rebuild for new webkit-sharp

* Wed Nov 25 2009 Götz Waschk <waschk@mandriva.org> 0.9.2-1mdv2010.1
+ Revision: 470016
- update to new version 0.9.2

* Wed Sep 16 2009 Götz Waschk <waschk@mandriva.org> 0.9.1-1mdv2010.0
+ Revision: 443468
- new version

* Fri Sep 04 2009 Götz Waschk <waschk@mandriva.org> 0.9.0-1mdv2010.0
+ Revision: 431010
- import gstreamer-sharp


* Fri Sep  4 2009 Götz Waschk <waschk@mandriva.org> 0.9.0-1mdv2010.0
- initial package
