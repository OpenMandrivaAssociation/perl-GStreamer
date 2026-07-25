%define upstream_name    GStreamer
%define upstream_version 0.21
Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:	1

Summary:    Perl module for the gstreamer library
License:    GPL+ or Artistic
Group:      Development/GNOME and GTK+
Url:        https://gtk2-perl.sf.net/
Source0:    https://cpan.metacpan.org/authors/id/X/XA/XAOC/GStreamer-0.21.tar.gz
# http://sourceforge.net/project/showfiles.php?group_id=64773&package_id=150831

BuildRequires:	make
BuildRequires: libgstreamer-devel >= 0.10
BuildRequires: perl-Glib >= 1.100
BuildRequires: perl-Gtk2 >= 1.100
BuildRequires: perl-ExtUtils-Depends
BuildRequires: perl-ExtUtils-PkgConfig
BuildRequires: perl-devel

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
