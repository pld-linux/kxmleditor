Summary:	kxmleditor - tool to display and edit contents of XML file for KDE
Summary(pl):	kxmleditor - narz�dzie do ogl�dania i edycji plik�w XML dla KDE
Name:		kxmleditor
Version:	1.1.0
Release:	2
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://dl.sourceforge.net/kxmleditor/%{name}-%{version}.tar.gz
# Source0-md5:	6c2f0acf7c434267040091ad356b0f04
Patch0:		%{name}-desktop.patch
URL:		http://kxmleditor.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KXML Editor is program, that display and edit contents of XML file.
Main features: Drag and drop editing, clipboard support, use of DOM
level 2 Qt library parser, KParts technology support, DCOP technology
support, editing KOffice compressed files.

%description -l pl
KXML Editor jest programem kt�ry wy�wietla i edytuje zawarto�� plik�w
XML. G��wne w�a�ciwo�ci: edycja drag&drop, wsparcie dla schowka,
u�ywanie parsera DOM z biblioteki Qt, wsparcie dla technologii KParts,
wsparcie dla technologii DCOP, edycja skompresowanych plik�w KOffice.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
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
