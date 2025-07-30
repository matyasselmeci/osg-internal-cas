Name:           osg-internal-cas
Version:        3
Release:        1%{?dist}
Summary:        OSG Internal CA certs

License:        Apache 2.0
URL:            https://github.com/osg-htc/osg-internal-cas

Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

%description
These are CA certificates for the internal use of OSG staff and collaborators.

%prep
%autosetup

%build
exit 0

%install
mkdir -p $RPM_BUILD_ROOT/etc/grid-security/certificates
mv certs/*.pem $RPM_BUILD_ROOT/etc/grid-security/certificates
mv certs/*.0 $RPM_BUILD_ROOT/etc/grid-security/certificates
mkdir -p $RPM_BUILD_ROOT/usr/share/%{name}
mv certs/*.crt $RPM_BUILD_ROOT/usr/share/%{name}


%files
/etc/grid-security/certificates/*
/usr/share/%{name}

%changelog
* Wed Jul 30 2025 Mátyás Selmeci <mselmeci@wisc.edu> - 3-1
- Add signing policy

* Fri Jun 13 2025 Mátyás Selmeci <mselmeci@wisc.edu> - 2-1
- Fix file extensions
- Include cert chains

* Fri Jun 13 2025 Mátyás Selmeci <mselmeci@wisc.edu> - 1-1
- Initial (SOFTWARE-6170)

