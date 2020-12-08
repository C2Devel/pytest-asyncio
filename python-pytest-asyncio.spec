%define pkgname pytest-asyncio
%global sum Pytest support for asyncio
%global descr Pytest support for asyncio

Name: python-%{pkgname}
Summary: %{sum}
Version: 0.9.0
Release: CROC1%{?dist}
License: Apache License, Version 2.0

Group: Development/Testing
URL: https://github.com/pytest-dev/pytest-asyncio
Source0: %{pkgname}-%{version}.tar.gz


BuildArch: noarch

%description
%{descr}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:       %{sum}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pkgname}
%{descr}


%prep
%setup -q -n %{pkgname}-%{version}


%build
%py3_build


%install
[ %buildroot = "/" ] || rm -rf %buildroot

%py3_install



%clean
rm -rf %{buildroot}


%files -n python%{python3_pkgversion}-%{pkgname}
%defattr(-,root,root,-)
%{python3_sitelib}/*

%doc README.rst LICENSE

%changelog
* Thu Dec 03 2020 Andrey Kulaev <adkulaev@gmail.com> 0.9.0-1
- Initial build.
