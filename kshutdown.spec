Summary:	KDE application for closing Linux
Summary(pl.UTF-8):	Aplikacja KDE do zamykania Linuksa
Name:		kshutdown
Version:	1.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kshutdown/%{name}-%{version}.tar.bz2
# Source0-md5:	dbacab8f1453599e9bad89e088248c68
Patch0:		%{name}-desktop.patch
URL:		http://kshutdown.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdelibs >= 3.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KShutDown helps closing and restarting Linux.

%description -l pl.UTF-8
KShutDown służy do zamykania lub restartowania systemu Linuks.

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

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/kshutdown
%{_datadir}/apps/kconf_update/kshutdown.upd
%{_libdir}/kde3/kshutdown*
%{_datadir}/apps/kshutdown
%{_iconsdir}/hicolor/*/apps/kshutdown.png
%{_desktopdir}/*.desktop
%{_datadir}/apps/kicker/applets/kshutdownlockout.desktop
