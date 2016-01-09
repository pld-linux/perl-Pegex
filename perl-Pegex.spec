#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Pegex
%include	/usr/lib/rpm/macros.perl
Summary:	Pegex - Acmeist PEG Parser Framework
Summary(pl.UTF-8):	Pegex - szkielet analizatora Acmeist PEG
Name:		perl-Pegex
Version:	0.60
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/I/IN/INGY/%{pdir}-%{version}.tar.gz
# Source0-md5:	347f72c1c0347148d80058ea35927df8
URL:		http://search.cpan.org/dist/Pegex/
BuildRequires:	perl-File-ShareDir-Install >= 0.06
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-YAML-LibYAML
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pegex is an Acmeist parser framework. It allows you to easily create
parsers that will work equivalently in lots of programming languages!
The inspiration for Pegex comes from the parsing engine upon which the
postmodern programming language Perl 6 is based on. Pegex brings this
beauty to the other justmodern languages that have a normal regular
expression engine available.

Pegex gets it name by combining Parsing Expression Grammars (PEG),
with Regular Expessions (Regex). That's actually what Pegex does.

%description -l pl.UTF-8
Pegex to szkielet analizatora Acmeist. Pozwala łatwo tworzyć
analizatory działające tak samo w wielu językach programowania. Pegex
jest zainspirowany silnikiem analizującym, na którym jest oparty
postmodernistyczny język Perl 6. Pegex dostarcza o piękno do innych
współczesnych języków, mających dostępny zwykły silnik wyrażeń
regularnych.

Nazwa Pegex pochodzi z połączenia skrótu PEG (Parsing Expression
Grammars) z Regex (Regular Expressions). I oznacza to, co właściwie
Pegex robi.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Pegex.pod

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Pegex.pm
%{perl_vendorlib}/Pegex
%{perl_vendorlib}/auto/share/dist/Pegex
%{_mandir}/man3/Pegex.3pm*
%{_mandir}/man3/Pegex::*.3pm*
%{_examplesdir}/%{name}-%{version}
