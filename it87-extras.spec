%if 0%{?fedora}
%global debug_package %{nil}
%endif

%global srcname it87
%global srcversion copr-staging

Name:     it87-extras
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Linux Driver for ITE LPC chips
License:  GPLv2
URL:      https://github.com/grandpares/it87


Source:   %{url}/archive/refs/heads/%{srcversion}.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Linux Driver for ITE LPC chips

%prep
%setup -q -c %{srcname}-%{srcversion}

%files
%doc %{srcname}-%{srcversion}/README
%license %{srcname}-%{srcversion}/LICENSE

%changelog
{{{ git_dir_changelog }}}
