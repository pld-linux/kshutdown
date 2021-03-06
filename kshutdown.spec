%define	kdever	4.6.2

Summary:	KDE application for closing Linux
Summary(pl.UTF-8):	Aplikacja KDE do zamykania Linuksa
Name:		kshutdown
Version:	2.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/kshutdown/%{name}-source-%{version}.zip
# Source0-md5:	af9d2bfda919e7712319e14e6ca89610
Patch0:		%{name}-desktop.patch
URL:		http://kshutdown.sourceforge.net/
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gettext-tools
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	phonon-devel >= 4.4.1
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KShutDown helps closing and restarting Linux.

%description -l pl.UTF-8
KShutDown służy do zamykania lub restartowania systemu Linuks.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

# remove unsupported locales
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{sr@ijekavian,sr@ijekavianlatin}

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
