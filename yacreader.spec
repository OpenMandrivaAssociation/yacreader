%global		_enable_debug_packages  %{nil}

%define		oname YACReader
#define		gitdate	20260501

Summary:	Cross platform comic reader and library manager
Name:	yacreader
Version:	10.0.0
Release:	1
# The entire source code is GPLv3+ except for:
# QsLog and folder_model (BSD) and pictureflow (MIT)
License:	GPLv3+ and BSD and MIT
Group:	Graphics
Url:	https://www.yacreader.com
Source0:	https://github.com/YACReader/yacreader/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:	yacreader-10.0.0-fix-systemd-unit-install-path.patch
BuildRequires:		cmake >= 3.25
BuildRequires:		make
BuildRequires:		qt6-qttools-linguist-tools
BuildRequires:		qt6-qtimageformats-devel
BuildRequires:		pkgconfig(gl)
BuildRequires:		pkgconfig(glu)
# For YACReaderLibrary QR Code display
BuildRequires:		pkgconfig(libqrencode)
BuildRequires:		pkgconfig(libunarr)
BuildRequires:		pkgconfig(poppler-qt6)
BuildRequires:		pkgconfig(Qt6Core) >= 6.7.0
BuildRequires:		pkgconfig(Qt6Core5Compat)
BuildRequires:		pkgconfig(Qt6Concurrent)
BuildRequires:		pkgconfig(Qt6Gui)
BuildRequires:		pkgconfig(Qt6Multimedia)
BuildRequires:		pkgconfig(Qt6Network)
BuildRequires:		pkgconfig(Qt6OpenGLWidgets)
BuildRequires:		pkgconfig(Qt6Qml)
BuildRequires:		pkgconfig(Qt6Quick)
BuildRequires:		pkgconfig(Qt6QuickControls2)
BuildRequires:		pkgconfig(Qt6QuickWidgets)
BuildRequires:		pkgconfig(Qt6ShaderTools)
BuildRequires:		pkgconfig(Qt6Svg)
BuildRequires:		pkgconfig(Qt6Sql)
BuildRequires:		pkgconfig(Qt6Test)
BuildRequires:		pkgconfig(Qt6TextToSpeech)
BuildRequires:		pkgconfig(Qt6Widgets)
BuildRequires:		pkgconfig(systemd)
BuildRequires:		pkgconfig(vulkan)
BuildRequires:		pkgconfig(xkbcommon)

%description
Best comic reader and comic manager with support for .cbr .cbz .zip .rar comic
files.

%files -f %{name}.lang -f %{name}library.lang -f %{name}libraryserver.lang
%license COPYING.txt
%doc CHANGELOG.md README.md
%{_bindir}/%{oname}
%{_bindir}/%{oname}Library
%{_bindir}/%{oname}LibraryServer
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/server/
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/applications/%{oname}Library.desktop
%{_iconsdir}/hicolor/scalable/apps/%{oname}.svg
%{_iconsdir}/hicolor/scalable/apps/%{oname}Library.svg
%{_userunitdir}/yacreaderlibraryserver.service
%{_mandir}/man1/%{oname}.1*
%{_mandir}/man1/%{oname}Library.1*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1



%build
%cmake	-DBUILD_TESTS=OFF \
					-DBUILD_SERVER_STANDALONE=OFF

%make_build


%install
%make_install -C build

# Translation files don't get installed: go manually
mkdir -p %{buildroot}%{_datadir}/%{name}/languages
pushd build/%{oname}
	cp *.qm %{buildroot}%{_datadir}/%{name}/languages
popd
pushd build/%{oname}Library
	cp *.qm %{buildroot}%{_datadir}/%{name}/languages
popd
pushd build/%{oname}LibraryServer
	cp *.qm %{buildroot}%{_datadir}/%{name}/languages 
popd

%find_lang %{name} --with-qt
%find_lang %{name}library --with-qt
%find_lang %{name}libraryserver --with-qt
