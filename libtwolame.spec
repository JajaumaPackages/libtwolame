Name:           libtwolame
Version:        0.3.13
Release:        1%{?dist}
Summary:        MPEG Audio Layer 2 (MP2) encoder

License:        LGPLv2.1
URL:            http://twolame.org
Source0:        http://downloads.sourceforge.net/project/twolame/twolame/%{version}/twolame-%{version}.tar.gz

BuildRequires:  libsndfile-devel

%description
TwoLAME is an optimized MPEG Audio Layer 2 (MP2) encoder. TwoLAME should be
able to be used as a drop-in replacement for LAME (a MPEG Layer 3 encoder). The
frontend takes very similar command line options to LAME, and the backend
library has a very similar API to LAME.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        -n twolame
Summary:        Command line twolame encoder tool

%description    -n twolame
This package provides a command line twolame encoder tool.


%prep
%setup -q -n twolame-%{version}


%build
%configure --disable-static

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_datadir}/doc/twolame/


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n twolame
%doc doc/psycho.txt doc/vbr.txt
%{_bindir}/*
%{_mandir}/man1/*.1*


%changelog
* Sun May 15 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.3.13-1
- Public release
