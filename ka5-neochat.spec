#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		neochat
Summary:	A Qt/QML based Matrix client
Summary(pl.UTF-8):	Klient usługi Matrix oparty na Qt/QML
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	3
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	de2af33caee8f1fb7bff97dde8dc9fdb
URL:		https://apps.kde.org/neochat/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Keychain-devel
BuildRequires:	Qt5Multimedia-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= 5.15.13
BuildRequires:	Qt5Quick-controls2-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.20
BuildRequires:	cmark-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.105.0
BuildRequires:	kf5-kconfig-devel >= 5.109.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.109.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.109.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.105.0
BuildRequires:	kf5-kdoctools >= 5.105.0
BuildRequires:	kf5-ki18n-devel >= 5.105.0
BuildRequires:	kf5-kio-devel >= 5.105.0
BuildRequires:	kf5-kirigami-addons-devel >= 0.7.2
BuildRequires:	kf5-kirigami2-devel >= 5.105.0
BuildRequires:	kf5-kitemmodels-devel >= 5.105.0
BuildRequires:	kf5-knotifications-devel >= 5.105.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.105.0
BuildRequires:	kf5-qqc2-desktop-style-devel >= 5.105.0
BuildRequires:	kf5-sonnet-devel >= 5.105.0
BuildRequires:	kquickimageeditor-devel
BuildRequires:	libQuotient-devel >= 0.7
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	qcoro-devel >= 0.4
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NeoChat is a client for Matrix (<https://matrix.org/>), the
decentralized communication protocol for instant messaging. It is a
fork of Spectral, using KDE frameworks, most notably Kirigami
(<https://invent.kde.org/frameworks/kirigami>) to provide a
convergent experience across multiple platforms.

NeoChat also make use of other KDE Frameworks as well as libQuotient
(<https://github.com/quotient-im/libQuotient>), a Qt-based SDK for the
Matrix Protocol (<https://spec.matrix.org/>).

%description -l pl.UTF-8
NeoChat to klient usługi Matrix (<https://matrix.org/>) -
zdecentralizowanego protokołu komunikatora internetowego. Jest to
odgałęzienie Spectral, wykorzystujące szkielety KDE, w szczególności
Kirigami (<https://invent.kde.org/frameworks/kirigami>), w celu
zapewnienia wygodnej obsługi na wielu platformach.

NeoChat wykorzystuje także inne szkielety KDE, a także libQuotient
(<https://github.com/quotient-im/libQuotient>) - oparte na Qt SDK dla
protokołu Matrix (<https://spec.matrix.org/>).

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# not supported by glibc yet (2.37)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ie,tok}

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/neochat
%{_desktopdir}/org.kde.neochat.desktop
%{_iconsdir}/hicolor/scalable/apps/org.kde.neochat.svg
%{_iconsdir}/hicolor/scalable/apps/org.kde.neochat.tray.svg
%{_datadir}/knotifications5/neochat.notifyrc
%{_datadir}/krunner/dbusplugins/plasma-runner-neochat.desktop
%lang(ca) %{_mandir}/ca/man1/neochat.1*
%lang(es) %{_mandir}/es/man1/neochat.1*
%lang(it) %{_mandir}/it/man1/neochat.1*
%{_mandir}/man1/neochat.1*
%lang(nl) %{_mandir}/nl/man1/neochat.1*
%lang(sv) %{_mandir}/sv/man1/neochat.1*
%lang(tr) %{_mandir}/tr/man1/neochat.1*
%lang(uk) %{_mandir}/uk/man1/neochat.1*
%{_datadir}/metainfo/org.kde.neochat.appdata.xml
%{_datadir}/qlogging-categories5/neochat.categories
