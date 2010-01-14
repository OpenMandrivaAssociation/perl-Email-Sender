%define upstream_name    Email-Sender
%define upstream_version 0.100110

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    An SMTP client that stays online
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Capture::Tiny)
BuildRequires: perl(Carp)
BuildRequires: perl(Cwd)
BuildRequires: perl(Email::Abstract)
BuildRequires: perl(Email::Address)
BuildRequires: perl(Email::Simple)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FindBin)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Moose)
BuildRequires: perl(Net::SMTP)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sys::Hostname::Long)
BuildRequires: perl(Throwable::Error)
BuildRequires: perl(Try::Tiny)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: perl(Throwable::Error)

%description
An Email::Sender::Success object is just an indicator that an email message
was successfully sent. Unless extended, it has no properties of its own.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


