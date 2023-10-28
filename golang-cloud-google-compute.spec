# Generated by go2rpm 1.6.0
%bcond_with check
%bcond_with bootstrap
%global debug_package %{nil}

# https://github.com/GoogleCloudPlatform/google-cloud-go
%global goipath         cloud.google.com/go/compute
%global forgeurl        https://github.com/GoogleCloudPlatform/google-cloud-go
Version:                1.23.2
%global tag             compute/v1.23.2
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Go packages for Google Cloud Platform services.}


%global golicenses      LICENSE
%global godocs          CHANGES.md CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        README.md RELEASING.md SECURITY.md testing.md\\\

Name:           %{goname}
Release:        %autorelease
Summary:        Google Cloud Client Libraries for Go

License:        BSD-3-Clause AND Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
# remove all modules but compute
find %{_builddir}/google-cloud-go-compute-v%{version}/* -depth -type d -not -path '*/compute*' -not -path '*/_build*' -exec rm -rf {} \;

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
%autochangelog
