%define _binary_payload w2.xzdio
%define __provides_exclude_from ^%{_datadir}/.*$

Name:       harbour-kalimba

Summary:    A Webview kalimba App
Version:    0.1.1
Release:    1
License:    LICENSE
BuildArch:  noarch
URL:        https://kalimba-online.ru/
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   libsailfishapp-launcher
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.3
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
Play the kalimba on SFOS

%if "%{?vendor}" == "chum"
PackageName: kalimba
Type: desktop-application
Categories:
 - Multimedia
PackagerName: Mark Washeim (poetaster)
Custom:
 - Repo: https://github.com/poetaster/harbour-kalimba
PackageIcon: https://raw.githubusercontent.com/poetaster/harbour-kalimba/main/icons/128x128/harbour-kalimba.png
Url:
 - Bugtracker: https://github.com/poetaster/harbour-kalimba/issues
Screenshots:
 - https://raw.githubusercontent.com/poetaster/harbour-kalimba/main/qml/html/img/mobile_srceen1.png
 - https://raw.githubusercontent.com/poetaster/harbour-kalimba/main/qml/html/img/mobile_srceen2.png
 - https://raw.githubusercontent.com/poetaster/harbour-kalimba/main/qml/html/img/mobile_srceen3.png
Links:
  Homepage: https://github.com/poetaster/harbour-kalimba
  Bugtracker: https://github.com/poetaster/harbour-kalimba/issues
  Donation: https://liberapay.com/poetaster
%endif

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5 

%make_build


%install
%qmake5_install


desktop-file-install --delete-original         --dir %{buildroot}%{_datadir}/applications                %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%defattr(0644,root,root,-)
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
