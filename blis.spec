#
Name     : blis
Version  : 0.2.1
Release  : 1
URL      : https://github.com/flame/blis/archive/0.2.1.tar.gz
Source0  : https://github.com/flame/blis/archive/0.2.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear


Patch1   : flags.patch

%description
![The BLIS cat is sleeping.](http://www.cs.utexas.edu/users/field/blis_cat.png)
[![Build Status](https://travis-ci.org/flame/blis.svg?branch=master)](https://travis-ci.org/flame/blis)

%prep
%setup -q -n blis-0.2.1
%patch1 -p1

pushd ..
cp -a blis-0.2.1 blis-haswell



%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1500260519

export CFLAGS="$CFLAGS -fopenmp -O3 -ffat-lto-objects -flto=4"

pushd ../blis-haswell
./configure   --prefix=/usr --enable-blas --enable-cblas --enable-threading=openmp --enable-shared  haswell
make V=1  %{?_smp_mflags}
popd
#pushd ../blis-skylake
#./configure   --enable-blas --enable-cblas --enable-threading=openmp --enable-shared  skylake
#make V=1  %{?_smp_mflags}
#popd


./configure  --prefix=/usr  --enable-blas --enable-cblas --enable-threading=openmp --enable-shared  reference
make V=1  %{?_smp_mflags}



%install
export SOURCE_DATE_EPOCH=1500260519
rm -rf %{buildroot}

pushd ../blis-haswell

%make_install

popd

%make_install


#mv %{buildroot}/builddir/blis  %{buildroot}/usr
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
mkdir -p  %{buildroot}/usr/lib64/haswell
mv %{buildroot}/usr/lib64/libblis-0.2.1-haswell.so %{buildroot}/usr/lib64/haswell/libblis.so.0.2.1
mv %{buildroot}/usr/lib64/libblis-0.2.1-reference.so %{buildroot}/usr/lib64/libblis.so.0.2.1
ln -sf libblis.so.0.2.1 %{buildroot}/usr/lib64/libblis.so

chmod a+x %{buildroot}/usr/lib64/*so*
chmod a+x %{buildroot}/usr/lib64/haswell/*so*



%files
%defattr(-,root,root,-)
/usr/include/blis/
/usr/lib64/haswell/libblis.so.0.2.1
/usr/lib64/libblis.so
/usr/lib64/libblis.so.0.2.1
