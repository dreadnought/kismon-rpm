Name:           kismon
Version:        0.5
Release:        2%{?dist}
Summary:        A simple GUI client for kismet

Group:          Applications/Internet
License:        BSD
URL:            http://www.salecker.org/software/kismon/en
Source0:        http://files.salecker.org/%{name}/%{name}-%{version}.tar.gz
Patch0:         kismon-desktop.patch
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  desktop-file-utils

Requires:       kismet
Requires:       python-osmgpsmap
Requires:       pygtk2
Requires:       python-simplejson
Requires:       pyclutter
    
%description
Kismon is a PyGTK Kismet Newcore client that creates a live map of the
networks. 

%prep
%setup -q
%patch0 -p1 -b .desktop
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
%doc README NEWS 
%{_bindir}/%{name}
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}*.egg-info
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon May 28 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.5-2
- License fixed
- Old stuff removed

* Tue Mar 27 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.5-1
- Initial package for Fedora
