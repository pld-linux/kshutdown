Summary:	KDE application for closing Linux
Summary(pl):	Aplikacja KDE do zamykania Linuksa
Name:		kshutdown
Version:	0.2.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kshutdown/%{name}-%{version}.tar.bz2
# Source0-md5:	72b9302d12217c24e21140b530ad3c91
URL:		http://kshutdown.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KShutDown helps closing and restarting Linux.

%description -l pl
KShutDown s³u¿y do zamykania lub restartowania systemu Linuks.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog FAQ FAQ.cs TODO
%attr(755,root,root) %{_bindir}/kshutdown
%{_datadir}/*
