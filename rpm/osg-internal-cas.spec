Name:           osg-internal-cas
Version:        1
Release:        1%{?dist}
Summary:        OSG Internal CA certs

License:        Apache 2.0
URL:            https://github.com/osg-htc/osg-internal-cas

Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  openssl

%description
These are CA certificates for the internal use of OSG staff and collaborators.

%prep
%autosetup

%build
exit 0

%install
mkdir -p $RPM_BUILD_ROOT/etc/grid-security/certificates
mv certs/"OSG Internal"*.crt $RPM_BUILD_ROOT/etc/grid-security/certificates
mv certs/*.0 $RPM_BUILD_ROOT/etc/grid-security/certificates


%files
%dir %attr(0755,root,root) /etc/grid-security/certificates
/etc/grid-security/certificates/*

%changelog
* Fri Jun 13 2025 Mátyás Selmeci <mselmeci@wisc.edu> - 1-1
- Initial (SOFTWARE-6170)

