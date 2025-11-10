%global		_enable_debug_packages  %{nil}

%define		oname YACReader
%define		gitdate	20251017

Summary:	Cross platform comic reader and library manager
Name:	yacreader
Version:	9.16.0
Release:	0.%{gitdate}.1
# The entire source code is GPLv3+ except:
# BSD (QsLog and folder_model) and MIT (pictureflow)
License:	GPLv3+ and BSD and MIT
Group:	Graphics
Url:	https://www.yacreader.com
Source0:	https://github.com/YACReader/yacreader/releases/download/%{version}/%{name}-%{version}-src.tar.xz
BuildRequires:		qt6-qttools-linguist-tools
BuildRequires:		qt6-qtimageformats-devel
BuildRequires:		pkgconfig(glu)
# For YACReaderLibrary QR Code display
#BuildRequires:		pkgconfig(libqrencode)
BuildRequires:		pkgconfig(libunarr)
BuildRequires:		pkgconfig(poppler-qt6)
BuildRequires:		pkgconfig(Qt6Core)
BuildRequires:		pkgconfig(Qt6Core5Compat)
BuildRequires:		pkgconfig(Qt6Concurrent)
BuildRequires:		pkgconfig(Qt6Gui)
BuildRequires:		pkgconfig(Qt6Multimedia)
BuildRequires:		pkgconfig(Qt6Network)
BuildRequires:		pkgconfig(Qt6OpenGLWidgets)
BuildRequires:		pkgconfig(Qt6QuickControls2)
BuildRequires:		pkgconfig(Qt6QuickWidgets)
BuildRequires:		pkgconfig(Qt6Svg)
BuildRequires:		pkgconfig(Qt6Sql)
BuildRequires:		pkgconfig(Qt6Test)
BuildRequires:		pkgconfig(Qt6Widgets)
BuildRequires:		pkgconfig(systemd)

%description
Best comic reader and comic manager with support for .cbr .cbz .zip .rar comic
files.

%files -f %{name}.lang -f %{name}library.lang
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
%set_build_flags
qmake-qt6 CONFIG+=unarr \
					CONFIG+=poppler \
					CONFIG+=server_standalone \
					PREFIX="%{_prefix}" \
					LIB="%{_libdir}"
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}

%find_lang %{name} --with-qt
%find_lang %{name}library --with-qt
