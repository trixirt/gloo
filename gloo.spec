%global commit0 01a0c815d1a98eb9b38341cf63546f234fbcc43b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20230824

Summary:        Communications library for AI/ML
Name:           gloo
License:        BSD-3-Clause
Version:        0.5.0^git%{date0}.%{shortcommit0}
Release:        1%{?dist}

URL:            https://github.com/facebookincubator/%{name}
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0:         0001-gloo-fedora-cmake-changes.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Gloo is a collective communications library. It comes with a number of
collective algorithms useful for machine learning applications. These
include a barrier, broadcast, and allreduce.

Transport of data between participating machines is abstracted so that
IP can be used at all times, or InifiniBand (or RoCE) when available.
In the latter case, if the InfiniBand transport is used, GPUDirect can
be used to accelerate cross machine GPU-to-GPU memory transfers.

Where applicable, algorithms have an implementation that works with
system memory buffers, and one that works with NVIDIA GPU memory buffers.
In the latter case, it is not necessary to copy memory between host and
device; this is taken care of by the algorithm implementations.

%package devel

Summary:        Headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/Gloo/docs
cp -p -r docs/* %{buildroot}%{_datadir}/Gloo/docs

%files
%dir %{_datadir}/Gloo
%license LICENSE
%doc README.md
%_libdir/lib%{name}.so.*

%files devel
%doc %{_datadir}/Gloo/docs/
%_includedir/%{name}/
%_libdir/cmake/Gloo/
%_libdir/lib%{name}.so

%changelog
* Fri Sep 22 2023 Tom Rix <trix@redhat.com> - 0.5.0^git20230824.01a0c81-1
- Initial package
