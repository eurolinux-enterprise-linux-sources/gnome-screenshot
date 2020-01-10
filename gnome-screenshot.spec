Name:           gnome-screenshot
Version:        3.8.3
Release:        3%{?dist}
Summary:        A screenshot utility for GNOME

Group:          Applications/System
License:        GPLv2+
URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/gnome-screenshot/3.8/gnome-screenshot-%{version}.tar.xz

BuildRequires: gtk3-devel
BuildRequires: libcanberra-devel
BuildRequires: intltool
BuildRequires: desktop-file-utils

Obsoletes: gnome-utils <= 1:3.3
Obsoletes: gnome-utils-libs <= 1:3.3
Obsoletes: gnome-utils-devel <= 1:3.3


%description
gnome-screenshot lets you take pictures of your screen.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# the desktop file contains Canonical 'enhancements' which don't validate :-(
# desktop-file-validate $RPM_BUILD_ROOT%%{_datadir}/applications/gnome-screenshot.desktop

%find_lang %{name}

%postun
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi


%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%files -f %{name}.lang
%doc COPYING
%{_bindir}/gnome-screenshot
%{_datadir}/GConf/gsettings/gnome-screenshot.convert
%{_datadir}/applications/gnome-screenshot.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-screenshot.gschema.xml
%doc %{_mandir}/man1/gnome-screenshot.1.gz

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.8.3-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.3-2
- Mass rebuild 2013-12-27

* Fri Jul 12 2013 Rui Matos <rmatos@redhat.com> - 3.8.3-1
- Update to 3.8.3
- Drop upstreamed patch

* Mon Jun 24 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.2-2
- Update man page

* Mon May 13 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Thu Feb 07 2013 Richard Hughes <rhughes@redhat.com> - 3.7.5-1
- Update to 3.7.5

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 3.7.4-1
- Update to 3.7.4

* Mon Nov 12 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Cosimo Cecchi <cosimoc@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Wed Sep 05 2012 Cosimo Cecchi <cosimoc@redhat.com> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 3.5.4-1
- Update to 3.5.4

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.2-1
- Update to 3.5.2

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-2
- Silence rpm scriptlet output

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Mon Apr  2 2012 Matthias Clasen <mclasen@redhat.com> - 3.4.0-2
- Add missing gsettings scriptlets (#808462)

* Mon Mar 26 2012 Cosimo Cecchi <cosimoc@redhat.com> - 3.4.0-1
- Update to 3.4.0

* Tue Mar 20 2012 Cosimo Cecchi <cosimoc@redhat.com> - 3.3.92-1
- Update to 3.3.92

* Tue Mar  6 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.91-1
- Update to 3.3.91

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.2-1
- Update to 3.3.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Matthias Clasen <mclasen@redhat.com> 3.3.1-2
- Fix the obsoletes to take epoch into account

* Wed Nov 23 2011 Matthias Clasen <mclasen@redhat.com> 3.3.1-1
- Initial packaging
