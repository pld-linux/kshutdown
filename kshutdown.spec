%define	prever	beta9

Summary:	KDE application for closing Linux
Summary(pl.UTF-8):	Aplikacja KDE do zamykania Linuksa
Name:		kshutdown
Version:	2.0
Release:	0.%{prever}.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kshutdown/%{name}-source-%{version}%{prever}.zip
# Source0-md5:	4a8a8f5f5e8323cf23ff37078d182d4e
Patch0:		%{name}-desktop.patch
URL:		http://kshutdown.sourceforge.net/
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdebase-workspace-devel
BuildRequires:	phonon-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KShutDown helps closing and restarting Linux.

%description -l pl.UTF-8
KShutDown służy do zamykania lub restartowania systemu Linuks.

%prep
%setup -q -n %{name}-%{version}%{prever}
%patch0 -p1

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-LIBTIDY_INCLUDE_DIR=%{_includedir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog TODO
%attr(755,root,root) %{_bindir}/kshutdown
%{_datadir}/apps/kshutdown
%{_desktopdir}/kde4/*.desktop
%{_iconsdir}/hicolor/*/apps/kshutdown.*
