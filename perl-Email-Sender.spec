%define upstream_name    Email-Sender
%define upstream_version 0.110001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	An SMTP client that stays online
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl-Capture-Tiny >= 0.80
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Email::Abstract)
BuildRequires:	perl(Email::Address)
BuildRequires:	perl(Email::Simple)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Net::SMTP)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Sys::Hostname::Long)
BuildRequires:	perl(Throwable::Error)
BuildRequires:	perl(Try::Tiny)

BuildArch:	noarch
Requires:	perl(Throwable::Error)

%description
An Email::Sender::Success object is just an indicator that an email message
was successfully sent. Unless extended, it has no properties of its own.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.110.1-2mdv2011.0
+ Revision: 657335
- rebuild for updated spec-helper

* Mon Apr 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.110.1-1
+ Revision: 650299
- update to new version 0.110001

* Fri Mar 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.110.0-1
+ Revision: 646333
- update to new version 0.110000

* Sun Oct 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.102.370-2mdv2011.0
+ Revision: 582690
- Add a dependency on the Capture-Tiny version

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.102.370-1mdv2011.0
+ Revision: 573792
- update to 0.102370

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.101.760-1mdv2011.0
+ Revision: 553019
- update to 0.101760

* Tue Feb 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.460-1mdv2010.1
+ Revision: 506745
- update to 0.100460

* Mon Feb 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.450-1mdv2010.1
+ Revision: 506238
- update to 0.100450

* Thu Jan 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.110-2mdv2010.1
+ Revision: 491214
- bump mkrel
- adding missing requires:

* Wed Jan 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.110-1mdv2010.1
+ Revision: 490494
- import perl-Email-Sender


* Wed Jan 13 2010 cpan2dist 0.100110-1mdv
- initial mdv release, generated with cpan2dist
