Name:           kismon
Version:        0.6
Release:        4%{?dist}
Summary:        A simple GUI client for kismet

Group:          Applications/Internet
License:        BSD
URL:            http://www.salecker.org/software/kismon/en
Source0:        http://files.salecker.org/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  desktop-file-utils

Requires:       kismet
Requires:       python-osmgpsmap
Requires:       pygtk2
Requires:       python-simplejson
    
%description
Kismon is a PyGTK Kismet Newcore client that creates a live map of the
networks. 

%prep
%setup -q
for lib in %{name}/*.py %{name}/windows/*.py; do
    sed '/\/usr\/bin\/env/d' $lib > $lib.new &&
    touch -r $lib $lib.new &&
    mv $lib.new $lib
done
chmod -x NEWS files/kismon.desktop
rm %{name}/windows/main.py

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root=%{buildroot}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc COPYING README NEWS 
%{_bindir}/%{name}
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}*.egg-info
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Oct 07 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-4
- Drop pyclutter because of its retirement in Fedora

* Wed Oct 03 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-3
- Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-1
- COPYING added
- Patch0 is now upstream
- Update to new upstream version 0.6

* Mon May 28 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.5-2
- License fixed
- Old stuff removed

* Tue Mar 27 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.5-1
- Initial package for Fedora
