#
# spec file for package aenigma-fonts (Version 1.0)
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           amharic_fonts
Version:        0.1
Release:        0
Summary:        Amharic free font collection by Natnael Getahun
License:        MIT
Group:          System/X11/Fonts
URL:		amharic-fonts-1.0.tar.xz#defunct

#DL-URL:	http://packages.debian.org/sid/ttf-aenigma
Source:         %{name}-v%{version}.tar.xz
BuildRequires:  fontpackages-devel
BuildRequires:	dos2unix
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       aenigma-0-fonts

%description
%{summary}.

%package -n AbyssinicaSIL-2.201
Group:          System/X11/Fonts
Summary:        AbyssinicaSIL free font collection

%description -n AbyssinicaSIL-2.201
This package contains:
* Abyssinica SIL

%package -n assets
Group:          System/X11/Fonts
Summary:        Selamta free font collection

%description -n assets
The fonts available are:
- Selamta

%prep
%setup -qn %name

%build
# no build needed.

%install
install -d %{buildroot}%{_ttfontsdir}
# by default install command uses 755 mode
install -m 644 */*.ttf %{buildroot}%{_ttfontsdir}
cp -a "%{S:2}" AbyssinicaSIL-2.201/OFL.txt

%files
%defattr(-,root,root)
%dir %{_ttfontsdir}
%{_ttfontsdir}/[0-9A-Za-z\-]*.ttf
%doc AbyssinicaSIL-2.201/OFL.txt

%files -n AbyssinicaSIL-2.201
%defattr(-,root,root)
%dir %{_ttfontsdir}
%{_ttfontsdir}/AbyssinicaSIL-2.201/web/[0-9A-Za-z\-]*.woff


%changelog
