%global modname it87-extras
%global srcversion master
%global srcname it87
%global pkgname it87

%if 0%{?fedora}
%global buildforkernels akmod
%global debug_package %{nil}
%endif

# name should have a -kmod suffix
Name:          %{pkgname}-kmod
Version:       %{srcversion}.git
Release:       2%{?dist}
Summary:       Linux Driver for ITE LPC chips
License:       GPLv2
URL:           https://github.com/frankcrawford/it87
Source0:       %{url}/archive/refs/heads/master.zip

BuildRequires: kmodtool

%{expand:%(kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Linux Driver for ITE LPC chips

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -c %{pkgname}
for kernel_version  in %{?kernel_versions} ; do
  cp -a %{srcname}-%{srcversion} _kmod_build_${kernel_version%%___*}/
done

%build
for kernel_version  in %{?kernel_versions} ; do
  pushd _kmod_build_${kernel_version%%___*}/
  make clean
  make KVER=${kernel_version%%___*}
  popd
done

%install
for kernel_version in %{?kernel_versions}; do
 mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/%{modname}.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/%{modname}.ko
done

# Blacklist:
install -p -m 0644 install/modprobe.conf %{buildroot}%{_prefix}/lib/modprobe.d/it87-crawford.conf

%{?akmod_install}

%changelog