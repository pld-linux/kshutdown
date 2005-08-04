Summary:	KDE application for closing Linux
Summary(pl):	Aplikacja KDE do zamykania Linuksa
Name:		kshutdown
Version:	0.6.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kshutdown/%{name}-%{version}.tar.bz2
# Source0-md5:	9a72132a316e38951bd8d84855ddeefc
Patch0:		%{name}-desktop.patch
URL:		http://kshutdown.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KShutDown helps closing and restarting Linux.

%description -l pl
KShutDown s³u¿y do zamykania lub restartowania systemu Linuks.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* admin
%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/*.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/kshutdown
%{_datadir}/apps/kconf_update/kshutdown.upd
%{_datadir}/apps/kshutdown
%{_iconsdir}/hicolor/*/apps/kshutdown.png
%{_desktopdir}/*.desktop
