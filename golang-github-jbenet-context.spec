%global goipath  github.com/jbenet/go-context
%global commit   d14ea06fba99483203c19d92cfcd13ebe73135f4
Version: 0

%global common_description %{expand:
Package context contains some extensions to go.net/context by @jbenet.}

%gometa

Name: %{goname}
Release: 0.3%{?dist}
Summary: Go context.Context extensions
License: MIT
URL: %{gourl}
Source0: %{gosource}
BuildRequires: golang(golang.org/x/net/context)

%description
%{common_description}

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q

%install
%goinstall

%check
%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitd14ea06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Dominik Mierzejewski <dominik@greysector.net> - 0-0.2.20180401gitd14ea06
- add missing BuildRequires
- fix Release in changelog entries

* Sun Apr 01 2018 Dominik Mierzejewski <dominik@greysector.net> - 0-0.1.20180401gitd14ea06
- First package for Fedora
