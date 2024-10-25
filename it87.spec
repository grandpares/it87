%if 0%{?fedora}
%global debug_package %{nil}
%endif

%global srcname it87

Name:     it87-extras
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Linux Driver for ITE LPC chips
License:  GPLv2
URL:      https://github.com/grandpares/it87


Source:   %{url}/archive/refs/heads/copr-staging.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Linux Driver for ITE LPC chips

%prep
%setup -q -c %{srcname}-master

%files
%doc %{srcname}-master/README
%license %{srcname}-master/LICENSE

%changelog
{{{ git_dir_changelog }}}
