#TODO:
#  - fix findlang
#  - place .desktop
#  - Fix why boils out:
#      kdecore (KLibLoader): WARNING: library=libkxmleditorpart: file=/usr/X11R6/lib/libkxmleditorpart.la: /usr/X11R6/lib/libkxmleditorpart.so.1: undefined symbol: languageChange__13DlgSearchBase
#      kxmleditor: FATAL: KXMLEditorShell::KXMLEditorShell no libkxmleditorpart found


Summary:	kxmleditor -  tool to display and edit contents of XML file for KDE
Summary(pl):	kxmleditor - narz�dzie do ogl�dania i edycji plik�w XML dla KDE.
Name:		kxmleditor
Version:	0.8.1
Release:	0.9
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz

URL:		http://%{name}.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%description
KXML Editor is program, that display and edit contents of XML file.
Main features: Drag and drop editing, clipboard support, use of DOM level
2 Qt library parser, KParts technology support, DCOP technology support,
editing KOffice compressed files.

%description -l pl
KXML Editor jest programem kt�ry wy�wietla i edytuje zawarto�� plik�w
XML. G��wne w�a�ciwo�ci: edycja drag&drop, wsparcie dla schowka,
u�ywanie parsera DOM z biblioteki Qt, wsparcie dla technologii KParts,
wsparcie dla technologii DCOP, edycja skompresowanych plik�w KOffice.

%prep
%setup -q

%build
#kde_htmldir="%{_htmldir}"; export kde_htmldir
#kde_icondir="%{_pixmapsdir}"; export kde_icondir
#kde_appsdir="%{_applnkdir}"; export kde_appsdir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

#install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/Databases
# mv $RPM_BUILD_ROOT%{_applnkdir}/Office/*.desktop $RPM_BUILD_ROOT/%{_applnkdir}/Office/Databases/

# %%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

# If we really need *.la ?
%attr(755,root,root) %{_libdir}/*

%{_datadir}/apps/%{name}
%{_datadir}/doc/HTML/en/%{name}
%{_applnkdir}/Applications/*.desktop

%{_datadir}/icons/*/*/apps/*
%{_datadir}/services/*.desktop
