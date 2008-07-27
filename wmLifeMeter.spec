Summary:	WindowMaker life progress meter
Summary(pl.UTF-8):	Monitor zużytego czasu życia dla WindowMakera
Name:		wmLifeMeter
Version:	0_4
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.samskivert.com/shaper/wmLifeMeter/%{name}-%{version}.tar.gz
# Source0-md5:	6b9efc5fc73afc584f9e23cd7a21cc53
URL:		http://www.samskivert.com/shaper/wmLifeMeter/
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple entertaining application for Linux that displays a person's
elapsed life as a real-time updating percentage to seven significant
digits such that the smallest digit ticks by while watched. Never
again let those precious seconds slip by un-noticed.

A great gift for those who have recently celebrated their 30th
birthday.

%description -l pl.UTF-8
Prosta aplikacja która wyświetla czas życia który upłynął danej osobie
jako uaktualniany na bieżąco do siódmej cyfry po przecinku licznik
procentowy, tak że widać jak kolejne cyfry zmieniają się w miarę
patrzenia. Nigdy więcej nie pozwól tym cennym sekundom upłynąć
niezauważonym.

Znakomity prezent dla tych którzy niedawno obchodzili 30. urodziny.

%prep
%setup -q -n %{name}

%build
cd src
%{__make} clean
%{__make} \
	CFLAGS="%{rpmcflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

cd src
install wmLifeMeter $RPM_BUILD_ROOT%{_bindir}
install wmLifeMeter.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man*/*
