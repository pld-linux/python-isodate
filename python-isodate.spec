#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# unit tests

%define 	module	isodate
Summary:	An ISO 8601 date/time/duration parser and formater
Summary(pl.UTF-8):	Moduł analizujący i formatujący daty/czas/okresy w formacie ISO 8601
Name:		python-%{module}
# 0.6.1 is expected to be last version for python2
Version:	0.6.1
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.simple/isodate/
Source0:	https://files.pythonhosted.org/packages/source/i/isodate/isodate-%{version}.tar.gz
# Source0-md5:	1a310658b30a48641bafb5652ad91c40
URL:		https://pypi.org/project/isodate/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-six
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	python3-six
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
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
Requires:	python3-modules >= 1:3.6

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

# tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/isodate/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.rst TODO.txt
%dir %{py_sitescriptdir}/isodate
%{py_sitescriptdir}/isodate/*.py[co]
%{py_sitescriptdir}/isodate-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.txt README.rst TODO.txt
%dir %{py3_sitescriptdir}/isodate
%{py3_sitescriptdir}/isodate/*.py
%{py3_sitescriptdir}/isodate/__pycache__
%{py3_sitescriptdir}/isodate-%{version}-py*.egg-info
%endif
