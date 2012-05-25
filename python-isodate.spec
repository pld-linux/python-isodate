%define 	module	isodate
Summary:	An ISO 8601 date/time/duration parser and formater
Summary(pl.UTF-8):	Moduł analizujący i formatujący daty/czas/okresy w formacie ISO 8601
Name:		python-%{module}
Version:	0.4.7
Release:	1
License:	GPL v3
Group:		Development/Languages
Source0:	http://pypi.python.org/packages/source/i/isodate/isodate-%{version}.tar.gz
# Source0-md5:	4ab330655445387b449de381f6ca864c
URL:		http://pypi.python.org/pypi/isodate/
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements ISO 8601 date, time and duration parsing. The
implementation follows ISO8601:2004 standard, and implements only
date/time representations mentioned in the standard. If something is
not mentioned there, then it is treated as non existent, and not as an
allowed option.

%description -l pl.UTF-8
Ten moduł zawiera implementację analizy daty, czasu i okresów w
formacie ISO 8601. Implementacja jest zgodna ze standardem
ISO8601:2004 i zawiera tylko reprezentacje daty/czasu opisane w
standardzie.

%prep
%setup -q -n isodate-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt TODO.txt
%dir %{py_sitescriptdir}/isodate
%{py_sitescriptdir}/isodate/*.py[co]
%{py_sitescriptdir}/isodate-%{version}-py*.egg-info
