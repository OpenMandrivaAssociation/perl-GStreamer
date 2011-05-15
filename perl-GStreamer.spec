%define upstream_name    GStreamer
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl module for the gstreamer library
License:    GPL+ or Artistic
Group:      Development/GNOME and GTK+
Url:        http://gtk2-perl.sf.net/
Source0:    http://downloads.sourceforge.net/gtk2-perl/%{upstream_name}-%{upstream_version}.tar.gz
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
perl Makefile.PL INSTALLDIRS=vendor

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
%make OPTIMIZE="$RPM_OPT_FLAGS"
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
