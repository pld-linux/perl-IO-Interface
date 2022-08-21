#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	IO
%define		pnam	Interface
Summary:	IO::Interface - Perl extension to access interface information
Summary(pl.UTF-8):	IO::Interface - rozszerzenie Perla do dostępu do informacji o interfejsach
Name:		perl-IO-Interface
Version:	1.09
Release:	4
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	806f97aff5a7361b6f54cd494f4cc9fd
URL:		https://metacpan.org/release/IO-Interface
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Interface adds methods to IO::Socket objects that allows them to
be used to retrieve and change information about the network
interfaces on your system.  In addition to the object-oriented access
methods, you can use a function-oriented style.

%description -l pl.UTF-8
IO::Interface dodaje do obiektów IO::Socket metody pozwalające na
używanie ich do pobierania i zmiany informacji o interfejsach
sieciowych w systemie. Oprócz metod zorientowanych obiektowo można
używać także wywołań zorientowanych na funkce.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--config optimize='%{rpmcflags}' \
	--installdirs=vendor

./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	--destdir $RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/IO/Interface/*.bs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorarch}/IO/Interface.pm
%dir %{perl_vendorarch}/IO/Interface
%{perl_vendorarch}/IO/Interface/Simple.pm
%dir %{perl_vendorarch}/auto/IO/Interface
%attr(755,root,root) %{perl_vendorarch}/auto/IO/Interface/Interface.so
%{_mandir}/man3/IO::Interface*.3pm*
