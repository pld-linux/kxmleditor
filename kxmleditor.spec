Summary:	kxmleditor - tool to display and edit contents of XML file for KDE
Summary(pl):	kxmleditor - narzêdzie do ogl±dania i edycji plików XML dla KDE
Name:		kxmleditor
Version:	1.0.0
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	0f34b6b8a5aa5781cb7f48c5fbcae10d
URL:		http://kxmleditor.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
KXML Editor is program, that display and edit contents of XML file.
Main features: Drag and drop editing, clipboard support, use of DOM
level 2 Qt library parser, KParts technology support, DCOP technology
support, editing KOffice compressed files.

%description -l pl
KXML Editor jest programem który wy¶wietla i edytuje zawarto¶æ plików
XML. G³ówne w³a¶ciwo¶ci: edycja drag&drop, wsparcie dla schowka,
u¿ywanie parsera DOM z biblioteki Qt, wsparcie dla technologii KParts,
wsparcie dla technologii DCOP, edycja skompresowanych plików KOffice.

%prep
%setup -q

%build
cp /usr/share/automake/config.sub admin

kde_htmldir="%{_htmldir}"; export kde_htmldir
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
	DESTDIR=$RPM_BUILD_ROOT

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
