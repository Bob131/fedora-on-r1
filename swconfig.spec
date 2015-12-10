%define with_cross    %{?_with_cross:         1} %{?!_with_cross:        0}

Name:           swconfig
Version:        15.05
Release:        1%{?dist}
Summary:        The program swconfig allows you to configure ethernet network switches.

Group:          System Environment/Base
License:        GPLv2
URL:            https://wiki.openwrt.org/doc/techref/swconfig
Source0:        swconfig-%{version}.tar.gz

Patch0:         swconfig.patch

BuildRequires:  libnl3-devel kernel-headers kernel-devel
%if %{with_cross}
BuildRequires: binutils-%{_build_arch}-linux-gnu, gcc-%{_build_arch}-linux-gnu
%define cross_opts CC=%{_build_arch}-linux-gnu-gcc
%endif

%description
CLI application from OpenWRT for configuring ethernet network switches

%prep
%setup -n %{name}
%patch0 -p1 -E

%build
make CFLAGS="-I %{_includedir} ${RPM_OPT_FLAGS}" %{?cross_opts} %{?_smp_mflags}

%install
%make_install

%files
%{_sbindir}/swconfig
