#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.01.95
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		neochat
Summary:	A Qt/QML based Matrix client
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	6675b907d431aa59bdb80c8f56612898
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= 5.15.0
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Keychain-devel
BuildRequires:	Qt6Multimedia-devel
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6Qml-devel >= 5.15.10
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	cmark-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 5.105.0
BuildRequires:	kf6-kconfig-devel >= 5.109.0
BuildRequires:	kf6-kconfigwidgets-devel >= 5.109.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.109.0
BuildRequires:	kf6-kdbusaddons-devel >= 5.105.0
BuildRequires:	kf6-kdoctools >= 5.105.0
BuildRequires:	kf6-ki18n-devel >= 5.105.0
BuildRequires:	kf6-kio-devel >= 5.105.0
BuildRequires:	kf6-kirigami-devel >= 5.105.0
BuildRequires:	kf6-kitemmodels-devel >= 5.105.0
BuildRequires:	kf6-knotifications-devel >= 5.105.0
BuildRequires:	kf6-kwindowsystem-devel >= 5.105.0
BuildRequires:	kf6-qqc2-desktop-style-devel >= 5.105.0
BuildRequires:	kf6-sonnet-devel >= 5.105.0
BuildRequires:	kirigami-addons-devel >= 0.7.2
BuildRequires:	kquickimageeditor-devel >= 0.3.0
BuildRequires:	libQuotient-qt6-devel >= 0.8.1.2-2
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qcoro-qt6-devel >= 0.4
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NeoChat is a client for [Matrix](https://matrix.org), the
decentralized communication protocol for instant messaging. It is a
fork of Spectral, using KDE frameworks, most notably
[Kirigami](https://invent.kde.org/frameworks/kirigami) to provide a
convergent experience across multiple platforms.

NeoChat also make use of other KDE Frameworks as well as
[libQuotient](https://github.com/quotient-im/libQuotient), a Qt-based
SDK for the [Matrix Protocol](https://spec.matrix.org/).

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
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
%{_datadir}/knotifications6/neochat.notifyrc
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
%{_datadir}/qlogging-categories6/neochat.categories
