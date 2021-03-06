#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : blis
Version  : 0.7.0
Release  : 8
URL      : https://github.com/flame/blis/archive/0.7.0/blis-0.7.0.tar.gz
Source0  : https://github.com/flame/blis/archive/0.7.0/blis-0.7.0.tar.gz
Summary  : BLAS-like Library Instantiation Software Framework
Group    : Development/Tools
License  : BSD-3-Clause
Requires: blis-data = %{version}-%{release}
Requires: blis-lib = %{version}-%{release}
Requires: blis-license = %{version}-%{release}

%description
BLIS is a portable software framework for instantiating high-performance
BLAS-like dense linear algebra libraries.

%package data
Summary: data components for the blis package.
Group: Data

%description data
data components for the blis package.


%package dev
Summary: dev components for the blis package.
Group: Development
Requires: blis-lib = %{version}-%{release}
Requires: blis-data = %{version}-%{release}
Provides: blis-devel = %{version}-%{release}
Requires: blis = %{version}-%{release}

%description dev
dev components for the blis package.


%package lib
Summary: lib components for the blis package.
Group: Libraries
Requires: blis-data = %{version}-%{release}
Requires: blis-license = %{version}-%{release}

%description lib
lib components for the blis package.


%package license
Summary: license components for the blis package.
Group: Default

%description license
license components for the blis package.


%prep
%setup -q -n blis-0.7.0
cd %{_builddir}/blis-0.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586914815
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}  -n ||:


%install
export SOURCE_DATE_EPOCH=1586914815
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/blis
cp %{_builddir}/blis-0.7.0/LICENSE %{buildroot}/usr/share/package-licenses/blis/dd70f1b19d38088817a9867b8c19a6672dec14ad
cp %{_builddir}/blis-0.7.0/build/templates/license.c %{buildroot}/usr/share/package-licenses/blis/d831d00068a357f16a5f607db0db75c8cde1f605
cp %{_builddir}/blis-0.7.0/build/templates/license.h %{buildroot}/usr/share/package-licenses/blis/d831d00068a357f16a5f607db0db75c8cde1f605
:
## install_append content

pushd build
../configure --disable-static --enable-shared --prefix=/usr \
--enable-blas --enable-cblas --enable-threading=openmp \
--libdir=/usr/lib64 penryn
make V=1 %{?_smp_mflags}
%make_install
LD_LIBRARY_PATH=%{buildroot}/usr/lib64 make check
popd

mkdir build-avx2
pushd build-avx2
export CFLAGS="$CFLAGS -march=haswell -mtune=haswell"
export CXXFLAGS="$CXXFLAGS -march=haswell -mtune-haswell"
../configure --disable-static --enable-shared --prefix=/usr \
--enable-blas --enable-cblas --enable-threading=openmp \
--libdir=/usr/lib64/haswell haswell
make V=1 %{?_smp_mflags}
%make_install
LD_LIBRARY_PATH=%{buildroot}/usr/lib64/haswell make check
popd

mkdir build-avx512
pushd build-avx512
export CFLAGS="$CFLAGS -march=skylake-avx512 -mtune=skylake"
export CXXFLAGS="$CXXFLAGS -march=haswell -mtune-haswell"
../configure --disable-static --enable-shared --prefix=/usr \
--enable-blas --enable-cblas --enable-threading=openmp \
--libdir=/usr/lib64/haswell/avx512_1 skx
make V=1 %{?_smp_mflags}
%make_install
LD_LIBRARY_PATH=%{buildroot}/usr/lib64/haswell/avx512_1 make check
popd
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/blis/common.mk
/usr/share/blis/config.mk
/usr/share/blis/config/haswell/make_defs.mk
/usr/share/blis/config/penryn/make_defs.mk
/usr/share/blis/config/skx/make_defs.mk

%files dev
%defattr(-,root,root,-)
/usr/include/blis/blis.h
/usr/include/blis/cblas.h
/usr/lib64/haswell/avx512_1/libblis.so
/usr/lib64/haswell/libblis.so
/usr/lib64/libblis.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libblis.so.3
/usr/lib64/haswell/avx512_1/libblis.so.3.0.0
/usr/lib64/haswell/libblis.so.3
/usr/lib64/haswell/libblis.so.3.0.0
/usr/lib64/libblis.so.3
/usr/lib64/libblis.so.3.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/blis/d831d00068a357f16a5f607db0db75c8cde1f605
/usr/share/package-licenses/blis/dd70f1b19d38088817a9867b8c19a6672dec14ad
