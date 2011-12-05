%define tarball xf86-video-tdfx
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:   Xorg X11 tdfx video driver
Name:      xorg-x11-drv-tdfx
Version:   1.4.3
Release:   1.1%{?dist}
URL:       http://www.x.org
License: MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Source1:   tdfx.xinf

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk 
#>= 1.4.99.1
BuildRequires: libdrm-devel >= 2.0-1
BuildRequires: xorg-x11-util-macros >= 1.1.5
BuildRequires: mesa-libGL-devel

Requires:  hwdata
Requires:  xorg-x11-server-Xorg >= 1.4.99.1

%description 
X.Org X11 tdfx video driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases/

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/tdfx_drv.so
%{_datadir}/hwdata/videoaliases/tdfx.xinf
%{_mandir}/man4/tdfx.4*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.4.3-1.1
- Rebuilt for RHEL 6

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 1.4.3-1
- tdfx 1.4.3

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 1.4.2-1.1
- ABI bump

* Thu Jul 02 2009 Adam Jackson <ajax@redhat.com> 1.4.2-1
- tdfx 1.4.2

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 1.4.1-1
- Latest upstream release

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 1.4.0-1
- Latest upstream release

* Wed Feb 27 2008 Dave Airlie <airlied@fedoraproject.org> - 1.3.0-8
- make tdfx build again by rebasing to upstream - may not work

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.0-7
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 1.3.0-6
- Rebuild for ppc toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.3.0-5
- Update Requires and BuildRequires.  Add Requires: hwdata.

* Mon Mar 19 2007 Adam Jackson <ajax@redhat.com> 1.3.0-4
- tdfx-1.3.0-fix-ddc-order.patch: Move DDC probe before mode validation.

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 1.3.0-3
- ExclusiveArch -> ExcludeArch

* Thu Nov 30 2006 Adam Jackson <ajax@redhat.com> 1.3.0-2.fc7
- Update to 1.3.0.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Fri May 26 2006 Mike A. Harris <mharris@redhat.com> 1.2,1-3
- Added "BuildRequires: libdrm-devel >= 2.0-1" for (#192358)

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 1.2.1-2
- Rebuild for 7.1 ABI fix.

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 1.2.1-1
- Update to 1.2.1 from 7.1RC1.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.1.1.3-1.3
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.1.1.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.1.1.3-1
- Updated xorg-x11-drv-tdfx to version 1.1.1.3 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.1.1.2-1
- Updated xorg-x11-drv-tdfx to version 1.1.1.2 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.1.1-1
- Updated xorg-x11-drv-tdfx to version 1.1.1 from X11R7 RC2

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 1.1.0.1-1
- Updated xorg-x11-drv-tdfx to version 1.1.0.1 from X11R7 RC1
- Fix *.la file removal.

* Tue Oct 4 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Limit "ExclusiveArch" to x86, x86_64

* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-0
- Initial spec file for tdfx video driver generated automatically
  by my xorg-driverspecgen script.
