Name:           gnome-screenshot
Version:        3.22.0
Release:        1%{?dist}
Summary:        A screenshot utility for GNOME

License:        GPLv2+
URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/gnome-screenshot/3.22/gnome-screenshot-%{version}.tar.xz

BuildRequires: gtk3-devel
BuildRequires: libcanberra-devel
BuildRequires: intltool
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

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
%make_install

%find_lang %{name}


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Screenshot.desktop


%postun
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi


%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%files -f %{name}.lang
%license COPYING
%{_bindir}/gnome-screenshot
%{_datadir}/GConf/gsettings/gnome-screenshot.convert
%{_datadir}/appdata/org.gnome.Screenshot.appdata.xml
%{_datadir}/applications/org.gnome.Screenshot.desktop
%{_datadir}/dbus-1/services/org.gnome.Screenshot.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-screenshot.gschema.xml
%{_mandir}/man1/gnome-screenshot.1*

%changelog
* Thu Feb 23 2017 Matthias Clasen <mclasen@redhat.com> - 3.22.0-1
- Rebase to 3.22.0
  Resolves: rhbz#1386956

* Mon Feb  8 2016 Rui Matos <rmatos@redhat.com> - 3.14.0-3
- Update Italian translation
Resolves: #1272498

* Thu May 14 2015 Rui Matos <rmatos@redhat.com> - 3.14.0-2
- Don't use colons in filenames
Resolves: #1162647

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Fri Sep 05 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-2.gitcbdd3f5
- Update to today's git snapshot (#1136959)

* Thu Aug 21 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90
- Validate the desktop file

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 25 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Tue Nov 19 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Richard Hughes <rhughes@redhat.com> - 3.9.4-1
- Update to 3.9.4

* Fri Jun 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.3-1
- Update to 3.9.3

* Tue May 14 2013 Richard Hughes <rhughes@redhat.com> - 3.8.2-1
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
