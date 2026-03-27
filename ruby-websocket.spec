#
# Conditional build:
%bcond_with	tests		# build without tests
%bcond_with	doc			# don't build ri/rdoc

%define pkgname websocket
Summary:	Universal Ruby library to handle WebSocket protocol
Name:		ruby-%{pkgname}
Version:	1.2.11
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	d4a209748d5d10c9ff88d199e8cdc1cb
URL:		http://github.com/imanel/websocket-ruby
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	rubygem(rspec)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Universal Ruby library to handle WebSocket protocol.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%if %{with tests}
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
