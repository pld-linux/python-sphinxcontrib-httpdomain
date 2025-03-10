#
# Conditional build:
%bcond_without	tests	# some test
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx domain for documenting HTTP APIs
Summary(pl.UTF-8):	Domena Sphinksa do dokumentacji API HTTP
Name:		python-sphinxcontrib-httpdomain
Version:	1.8.1
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-httpdomain/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-httpdomain/sphinxcontrib-httpdomain-%{version}.tar.gz
# Source0-md5:	68fb25d99bb6cf1987ca8f24c0cb5dd2
URL:		https://pypi.org/project/sphinxcontrib-httpdomain/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.6
BuildRequires:	python-pytest
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.6
BuildRequires:	python3-pytest
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The contrib extension sphinxcontrib.httpdomain, provides a Sphinx
domain for describing HTTP APIs.

%description -l pl.UTF-8
Dodatkowe rozszerzenie sphinxcontrib.httpdomain udostępnia domenę
Sphinksa do opisu API HTTP.

%package -n python3-sphinxcontrib-httpdomain
Summary:	Sphinx domain for documenting HTTP APIs
Summary(pl.UTF-8):	Domena Sphinksa do dokumentacji API HTTP
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-sphinxcontrib-httpdomain
The contrib extension sphinxcontrib.httpdomain, provides a Sphinx
domain for describing HTTP APIs.

%description -n python3-sphinxcontrib-httpdomain -l pl.UTF-8
Dodatkowe rozszerzenie sphinxcontrib.httpdomain udostępnia domenę
Sphinksa do opisu API HTTP.

%prep
%setup -q -n sphinxcontrib-httpdomain-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest test
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest test
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/sphinxcontrib/locale/httpdomain.pot
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/sphinxcontrib/locale/*/LC_MESSAGES/httpdomain.po
%endif

%if %{with python3}
%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/sphinxcontrib/locale/httpdomain.pot
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/sphinxcontrib/locale/*/LC_MESSAGES/httpdomain.po
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/sphinxcontrib/httpdomain.py[co]
%{py_sitescriptdir}/sphinxcontrib/autohttp
%dir %{py_sitescriptdir}/sphinxcontrib/locale
%lang(es) %{py_sitescriptdir}/sphinxcontrib/locale/es_ES
%lang(fr) %{py_sitescriptdir}/sphinxcontrib/locale/fr_FR
%{py_sitescriptdir}/sphinxcontrib_httpdomain-%{version}-py*.egg-info
%{py_sitescriptdir}/sphinxcontrib_httpdomain-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-sphinxcontrib-httpdomain
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/sphinxcontrib/httpdomain.py
%{py3_sitescriptdir}/sphinxcontrib/__pycache__/httpdomain.cpython-*.py[co]
%{py3_sitescriptdir}/sphinxcontrib/autohttp
%dir %{py3_sitescriptdir}/sphinxcontrib/locale
%lang(es) %{py3_sitescriptdir}/sphinxcontrib/locale/es_ES
%lang(fr) %{py3_sitescriptdir}/sphinxcontrib/locale/fr_FR
%{py3_sitescriptdir}/sphinxcontrib_httpdomain-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_httpdomain-%{version}-py*-nspkg.pth
%endif
