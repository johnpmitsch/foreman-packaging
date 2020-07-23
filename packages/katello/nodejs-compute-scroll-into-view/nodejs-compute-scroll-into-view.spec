%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name compute-scroll-into-view

Name: %{?scl_prefix}nodejs-compute-scroll-into-view
Version: 1.0.14
Release: 1%{?dist}
Summary: The engine that powers scroll-into-view-if-needed
License: MIT
Group: Development/Libraries
URL: https://scroll-into-view-if-needed.netlify.com
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr es %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr typings %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr umd %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
* Tue Jul 21 2020 John Mitsch <jomitsch@redhat.com> 1.0.14-1
- Add nodejs-compute-scroll-into-view generated by npm2rpm using the single strategy

