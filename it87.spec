%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     it87-extras
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Linux Driver for ITE LPC chips
License:  GPLv2
URL:      https://github.com/frankcrawford/it87


Source:   %{url}/archive/refs/heads/master.tar.gz
Source1:  ./modprobe.conf

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Linux Driver for ITE LPC chips

%prep
%setup -q -c %{name}-master

%files
%doc %{name}-master/README.md
%license %{name}-master/LICENSE

%changelog
{{{ git_dir_changelog }}}
