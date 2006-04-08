#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IO
%define		pnam	Interface
Summary:	perl(IO::Interface) perl extension to access interface information
Name:		perl-IO-Interface
Version:	0.98
Release:	0.1
License:	GPL v2/Artistic (same as perl)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	91d5029a32302aa02414c9c8e3353cec
URL:		http://search.cpan.org/dist/IO-Interface
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
#%%if %%{with autodeps} || %%{with tests}
#%%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
IO::Interface adds methods to IO::Socket objects that allows them to
be used to retrieve and change information about the network
interfaces on your system.  In addition to the object-oriented access
methods, you can use a function-oriented style.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/IO/Interface.pm
%dir %{perl_vendorarch}/auto/IO/Interface
%attr(755,root,root) %{perl_vendorarch}/auto/IO/Interface/*so
%{perl_vendorarch}/auto/IO/Interface/*bs
%{_mandir}/man3/*
