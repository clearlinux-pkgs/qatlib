#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qatlib
Version  : 22.07.0
Release  : 1
URL      : https://github.com/intel/qatlib/archive/refs/tags/22.07.0.tar.gz
Source0  : https://github.com/intel/qatlib/archive/refs/tags/22.07.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: qatlib-bin = %{version}-%{release}
Requires: qatlib-lib = %{version}-%{release}
Requires: qatlib-license = %{version}-%{release}
Requires: qatlib-man = %{version}-%{release}
Requires: qatlib-services = %{version}-%{release}
BuildRequires : openssl-dev
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(zlib)
BuildRequires : yasm

%description
# Intel&reg; QuickAssist Technology Library (QATlib)
## Table of Contents
- [Revision History](#revision-history)
- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Supported Devices](#supported-devices)
- [Limitations](#limitations)
- [Environmental Assumptions](#environmental-assumptions)
- [Examples](#examples)
- [Open Issues](#open-issues)
- [Resolved Issues](#resolved-issues)
- [Licensing](#licensing)
- [Legal](#legal)
- [Terminology](#terminology)

%package bin
Summary: bin components for the qatlib package.
Group: Binaries
Requires: qatlib-license = %{version}-%{release}
Requires: qatlib-services = %{version}-%{release}

%description bin
bin components for the qatlib package.


%package dev
Summary: dev components for the qatlib package.
Group: Development
Requires: qatlib-lib = %{version}-%{release}
Requires: qatlib-bin = %{version}-%{release}
Provides: qatlib-devel = %{version}-%{release}
Requires: qatlib = %{version}-%{release}

%description dev
dev components for the qatlib package.


%package lib
Summary: lib components for the qatlib package.
Group: Libraries
Requires: qatlib-license = %{version}-%{release}

%description lib
lib components for the qatlib package.


%package license
Summary: license components for the qatlib package.
Group: Default

%description license
license components for the qatlib package.


%package man
Summary: man components for the qatlib package.
Group: Default

%description man
man components for the qatlib package.


%package services
Summary: services components for the qatlib package.
Group: Systemd services

%description services
services components for the qatlib package.


%prep
%setup -q -n qatlib-22.07.0
cd %{_builddir}/qatlib-22.07.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1659459023
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1659459023
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qatlib
cp %{_builddir}/qatlib-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/qatlib/154c1d177e5fcb47563a47d8a17b7b5548ad9072
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/qat_init.sh
/usr/bin/qatmgr

%files dev
%defattr(-,root,root,-)
/usr/include/qat/cpa.h
/usr/include/qat/cpa_cy_common.h
/usr/include/qat/cpa_cy_dh.h
/usr/include/qat/cpa_cy_drbg.h
/usr/include/qat/cpa_cy_dsa.h
/usr/include/qat/cpa_cy_ec.h
/usr/include/qat/cpa_cy_ecdh.h
/usr/include/qat/cpa_cy_ecdsa.h
/usr/include/qat/cpa_cy_im.h
/usr/include/qat/cpa_cy_key.h
/usr/include/qat/cpa_cy_kpt.h
/usr/include/qat/cpa_cy_ln.h
/usr/include/qat/cpa_cy_nrbg.h
/usr/include/qat/cpa_cy_prime.h
/usr/include/qat/cpa_cy_rsa.h
/usr/include/qat/cpa_cy_sym.h
/usr/include/qat/cpa_cy_sym_dp.h
/usr/include/qat/cpa_dc.h
/usr/include/qat/cpa_dc_chain.h
/usr/include/qat/cpa_dc_dp.h
/usr/include/qat/cpa_dev.h
/usr/include/qat/cpa_types.h
/usr/include/qat/icp_sal.h
/usr/include/qat/icp_sal_congestion_mgmt.h
/usr/include/qat/icp_sal_poll.h
/usr/include/qat/icp_sal_user.h
/usr/include/qat/icp_sal_versions.h
/usr/include/qat/qae_mem.h
/usr/lib64/libqat.so
/usr/lib64/libusdm.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libqat.so.3
/usr/lib64/libqat.so.3.0.0
/usr/lib64/libusdm.so.0
/usr/lib64/libusdm.so.0.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qatlib/154c1d177e5fcb47563a47d8a17b7b5548ad9072

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/qat_init.sh.8
/usr/share/man/man8/qatmgr.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/qat.service
