#
# Conditional build:
%bcond_with	tests		# build without tests
%bcond_with	doc			# don't build ri/rdoc

%define pkgname websocket
Summary:	Universal Ruby library to handle WebSocket protocol
Name:		ruby-%{pkgname}
Version:	1.2.2
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	d75d6d4097a705d9c5ff5bc2a6546103
URL:		http://github.com/imanel/websocket-ruby
Patch0:		comment-broken-tests.patch
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
%endif
BuildRequires:	rubygem(rspec)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Universal Ruby library to handle WebSocket protocol.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p0

%build
# write .gemspec
%__gem_helper spec

%if %{with tests}
find spec -name *.rb | xargs sed -i '/its/ s/^/#/'
rspec -Ilib spec
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
