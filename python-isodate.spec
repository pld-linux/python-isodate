#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# unit tests

%define 	module	isodate
Summary:	An ISO 8601 date/time/duration parser and formater
Summary(pl.UTF-8):	Moduł analizujący i formatujący daty/czas/okresy w formacie ISO 8601
Name:		python-%{module}
Version:	0.5.4
Release:	5
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/isodate/
Source0:	https://pypi.python.org/packages/source/i/isodate/isodate-%{version}.tar.gz
# Source0-md5:	9da3ea2af54a6261d854e73d2266030e
URL:		https://pypi.python.org/pypi/isodate/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-2to3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
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

%package -n python3-%{module}
Summary:	An ISO 8601 date/time/duration parser and formater
Summary(pl.UTF-8):	Moduł analizujący i formatujący daty/czas/okresy w formacie ISO 8601
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
This module implements ISO 8601 date, time and duration parsing. The
implementation follows ISO8601:2004 standard, and implements only
date/time representations mentioned in the standard. If something is
not mentioned there, then it is treated as non existent, and not as an
allowed option.

%description -n python3-%{module} -l pl.UTF-8
Ten moduł zawiera implementację analizy daty, czasu i okresów w
formacie ISO 8601. Implementacja jest zgodna ze standardem
ISO8601:2004 i zawiera tylko reprezentacje daty/czasu opisane w
standardzie.

%prep
%setup -q -n isodate-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
# tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/isodate/tests
%endif

%if %{with python3}
%py3_install

# redundant
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/isodate.egg-info
# tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/isodate/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.rst TODO.txt
%dir %{py_sitescriptdir}/isodate
%{py_sitescriptdir}/isodate/*.py[co]
%{py_sitescriptdir}/isodate-%{version}-py*.egg-info

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.txt README.rst TODO.txt
%dir %{py3_sitescriptdir}/isodate
%{py3_sitescriptdir}/isodate/*.py
%{py3_sitescriptdir}/isodate/__pycache__
%{py3_sitescriptdir}/isodate-%{version}-py*.egg-info
