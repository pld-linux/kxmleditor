Summary:	kxmleditor - tool to display and edit contents of XML file for KDE
Summary(pl.UTF-8):	kxmleditor - narzędzie do oglądania i edycji plików XML dla KDE
Name:		kxmleditor
Version:	1.1.4
Release:	2
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://dl.sourceforge.net/kxmleditor/%{name}-%{version}.tar.gz
# Source0-md5:	d2329e06393c78f22531b8ba42e67d9b
Source1:	http://ep09.pld-linux.org/~djurban/kde/kde-common-admin.tar.bz2
# Source1-md5:	e5c75ce22f1525b13532b519ae88e7a4
Patch0:		%{name}-desktop.patch
URL:		http://kxmleditor.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KXML Editor is program, that display and edit contents of XML file.
Main features: Drag and drop editing, clipboard support, use of DOM
level 2 Qt library parser, KParts technology support, DCOP technology
support, editing KOffice compressed files.

%description -l pl.UTF-8
KXML Editor jest programem który wyświetla i edytuje zawartość plików
XML. Główne właściwości: edycja drag&drop, wsparcie dla schowka,
używanie parsera DOM z biblioteki Qt, wsparcie dla technologii KParts,
wsparcie dla technologii DCOP, edycja skompresowanych plików KOffice.

%prep
%setup -q -a1
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin

%configure \
	--enable-final \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--with-qt-libraries=%{_libdir} \
	--with-xinerama

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}


mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
# KDE module, (lt_)dlopened - .la needed
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_libdir}/*.la
%{_datadir}/apps/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/services/*.desktop
