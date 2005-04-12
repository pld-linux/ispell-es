Summary:	Spanish dictionary for ispell
Summary(ca):	Diccionari espanyol per a ispell
Summary(es):	Diccionario español para ispell
Summary(pl):	Hiszpañski s³ownik dla ispell
Name:		ispell-es
Version:	1.8
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.datsi.fi.upm.es/~coes/espa~nol-%{version}.tar.gz
# Source0-md5:	625507dca3da835964b0b8a932e3f4e1
URL:		http://www.datsi.fi.upm.es/~coes/espell_leame/espell_leame.html
BuildRequires:	ispell >= 3.1.13
Requires:	ispell >= 3.1.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spanish dictionary for ispell.

%description -l ca
Diccionari espanyol per a ispell.

%description -l es
Diccionario español para ispell.

%description -l pl
Hiszpañski s³ownik dla programu ispell.

%prep
%setup -q -n espa~nol-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ispell

install espa~nol.aff $RPM_BUILD_ROOT%{_libdir}/ispell/spanish.aff
install espa~nol.hash $RPM_BUILD_ROOT%{_libdir}/ispell/spanish.hash

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%lang(es) %doc LEAME
%{_libdir}/ispell/*
