%global debug_package %{nil}

Name: python-urllib3
Epoch: 100
Version: 1.26.9
Release: 1%{?dist}
BuildArch: noarch
Summary: Python HTTP library with thread-safe connection pooling and file post
License: MIT
URL: https://github.com/urllib3/urllib3/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: ca-certificates
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Python3 HTTP module with connection pooling and file POST abilities.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python_version_nodots}-urllib3
Summary: Python HTTP library with thread-safe connection pooling and file post
Requires: python3
Provides: python3-urllib3 = %{epoch}:%{version}-%{release}
Provides: python3dist(urllib3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-urllib3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(urllib3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-urllib3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(urllib3) = %{epoch}:%{version}-%{release}

%description -n python%{python_version_nodots}-urllib3
Python3 HTTP module with connection pooling and file POST abilities.

%files -n python%{python_version_nodots}-urllib3
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-urllib3
Summary: Python HTTP library with thread-safe connection pooling and file post
Requires: python3
Provides: python3-urllib3 = %{epoch}:%{version}-%{release}
Provides: python3dist(urllib3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-urllib3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(urllib3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-urllib3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(urllib3) = %{epoch}:%{version}-%{release}

%description -n python3-urllib3
Python3 HTTP module with connection pooling and file POST abilities.

%files -n python3-urllib3
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog
