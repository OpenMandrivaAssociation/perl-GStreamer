%define upstream_name    GStreamer
%define upstream_version 0.18
Name:       perl-%{upstream_name}
Version:    %perl_convert_version 0.18
Release:	2

Summary:    Perl module for the gstreamer library
License:    GPL+ or Artistic
Group:      Development/GNOME and GTK+
Url:        http://gtk2-perl.sf.net/
Source0:    http://sourceforge.net/projects/gtk2-perl/files/GStreamer/0.18/GStreamer-0.18.tar.gz
# http://sourceforge.net/project/showfiles.php?group_id=64773&package_id=150831

BuildRequires: libgstreamer-devel >= 0.10
BuildRequires: perl-Glib >= 1.100
BuildRequires: perl-Gtk2 >= 1.100
BuildRequires: perl-ExtUtils-Depends
BuildRequires: perl-ExtUtils-PkgConfig
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module allows you to use the GStreamer library from Perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -rf 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%optflags" OTHERLDFLAGS="-Wl,--as-needed"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/%{upstream_name}*
%{perl_vendorarch}/auto/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.160.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 15 2011 Funda Wang <fwang@mandriva.org> 0.160.0-2
+ Revision: 674807
- use flags

* Sun May 15 2011 Funda Wang <fwang@mandriva.org> 0.160.0-1
+ Revision: 674795
- new version 0.16

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-2mdv2011.0
+ Revision: 555883
- rebuild for perl 5.12

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.0
+ Revision: 408414
- rebuild using %%perl_convert_version

* Mon Feb 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2009.1
+ Revision: 344039
- update to new version 0.15

* Mon Jan 19 2009 Thierry Vignaud <tv@mandriva.org> 0.14-1mdv2009.1
+ Revision: 331121
- new release

* Wed Dec 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2009.1
+ Revision: 315107
- update to new version 0.13

* Fri Nov 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2009.1
+ Revision: 307396
- update to new version 0.12

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.11-2mdv2009.0
+ Revision: 268512
- rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.0
+ Revision: 202295
- new version
- update to new version 0.11

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 0.10-1mdv2009.0
+ Revision: 192888
- new release

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.09-2mdv2008.1
+ Revision: 152099
- rebuild

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 0.09-1mdv2008.1
+ Revision: 135846
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Aug 11 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.09-1mdv2007.0
- new release

* Wed Jul 26 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.08-1mdv2007.0
- new release

* Wed Mar 22 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.07-1mdk
- new release

* Tue Jan 31 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.06-1mdk
- new release

* Thu Dec 08 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.05-1mdk
- new release

* Wed Oct 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-4mdk
- Fix BuildRequires

* Tue Oct 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-3mdk
- Fix BuildRequires

* Tue Oct 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-2mdk
- BuildRequires fix

* Tue Oct 04 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.04-1mdk
- initial release


