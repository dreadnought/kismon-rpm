Name:           kismon
Version:        0.8.1
Release:        1%{?dist}
Summary:        A simple GUI client for kismet

License:        BSD
URL:            https://www.salecker.org/software/kismon.html
Source0:        https://files.salecker.org/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils

Requires:       osm-gps-map-gobject
Requires:       pygobject3
Requires:       python3-cairo
Requires:       python3-simplejson

Recommends:     kismet

%description
Kismon is GUI client for kismet (wireless scanner/sniffer/monitor) with
several features:
* a live map of the networks
* file import: netxml (kismet), csv (old kismet version), json (kismon)
* file export: kmz (Google Earth) and all import formats
* signal graph for each network
* it can connect to multiple kismet servers simultaneously

%prep
%setup -q
for lib in %{name}/*.py %{name}/windows/*.py; do
    sed '/\/usr\/bin\/env/d' $lib > $lib.new &&
    touch -r $lib $lib.new &&
    mv $lib.new $lib
done
chmod -x files/kismon.desktop

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
* Sat Jul 02 2016 Patrick Salecker <mail@salecker.org> - 0.8.1-1
- Update to new upstream version 0.8.1
- osm-gps-map dependency fixed
- Website URL and description updated

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

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
