# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-urllib3
Epoch: 100
Version: 2.3.0
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

%if 0%{?suse_version} > 1500 || 0%{?rhel} == 7
%package -n python%{python3_version_nodots}-urllib3
Summary: Python HTTP library with thread-safe connection pooling and file post
Requires: python3
Provides: python3-urllib3 = %{epoch}:%{version}-%{release}
Provides: python3dist(urllib3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-urllib3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(urllib3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-urllib3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(urllib3) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-urllib3
Python3 HTTP module with connection pooling and file POST abilities.

%files -n python%{python3_version_nodots}-urllib3
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
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

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000) && !(0%{?rhel} == 7)
%package -n python3-urllib3
Summary: Python HTTP library with thread-safe connection pooling and file post
Requires: python3
Requires: python3-urllib3+socks = %{epoch}:%{version}-%{release}
Provides: python3-urllib3 = %{epoch}:%{version}-%{release}
Provides: python3dist(urllib3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-urllib3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(urllib3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-urllib3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(urllib3) = %{epoch}:%{version}-%{release}

%description -n python3-urllib3
Python3 HTTP module with connection pooling and file POST abilities.

%package -n python3-urllib3+brotli
Summary: Metapackage for python3-urllib3: brotli extras
Requires: python3-brotli >= 1.0.9
Requires: python3-urllib3 = %{epoch}:%{version}-%{release}

%description -n python3-urllib3+brotli
This is a metapackage bringing in brotli extras requires for
python3-urllib3. It makes sure the dependencies are installed.

%package -n python3-urllib3+socks
Summary: Metapackage for python3-urllib3: socks extras
Requires: python3-pysocks >= 1.5.6
Requires: python3-urllib3 = %{epoch}:%{version}-%{release}

%description -n python3-urllib3+socks
This is a metapackage bringing in socks extras requires for
python3-urllib3. It makes sure the dependencies are installed.

%files -n python3-urllib3
%license LICENSE.txt
%{python3_sitelib}/*

%files -n python3-urllib3+brotli
%license LICENSE.txt

%files -n python3-urllib3+socks
%license LICENSE.txt
%endif

%changelog