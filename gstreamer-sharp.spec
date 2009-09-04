%define name gstreamer-sharp
%define version 0.9.0
%define release %mkrel 1
%define api 0.10

Summary: C#/CLI bindings for GStreamer
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://gstreamer.freedesktop.org/src/%name/%{name}-%{version}.tar.bz2
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
