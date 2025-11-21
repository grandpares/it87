%global srcname it87
%global pkgname it87-extras
%global maintainer grandpares

Name:           akmod-%{pkgname}
Version:       {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Linux driver for ITE LPC chips
License:        GPLv2
URL:            https://github.com/%{maintainer}/it87
Source0:        %{url}/archive/refs/heads/akmods.zip

BuildRequires:  kmodtool
BuildRequires:  make
BuildRequires:  gcc

%description
Linux driver for ITE LPC chips (akmod source package).

%prep
%autosetup -c %{pkgname}

%build
# NO kernel modules built here – this is an akmod package.

%install
# Install source into akmods directory
install -d %{buildroot}/usr/src/akmods/%{pkgname}-%{version}/
cp -a %{srcname}-akmods/* %{buildroot}/usr/src/akmods/%{pkgname}-%{version}/

%{?akmod_install}

%files
/usr/src/akmods/%{pkgname}-%{version}/
%doc
%license
