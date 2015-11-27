Name:           kismon
Version:        0.7
Release:        1%{?dist}
Summary:        A simple GUI client for kismet

License:        BSD
URL:            http://www.salecker.org/software/kismon/en
Source0:        http://files.salecker.org/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils

Requires:       kismet
Requires:       osm-gps-map
Requires:       pygobject3
Requires:       python3-cairo
Requires:       python3-simplejson
    
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
%py3_build

%install
%py3_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc COPYING README NEWS 
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.egg-info
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Nov 27 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.7-1
- Update to new upstream version 0.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 29 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-7
- osm-gps-map is the replacement for python-osmgpsmap

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 07 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-4
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
