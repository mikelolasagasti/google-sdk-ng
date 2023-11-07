# Generated by go2rpm 1.10.0
%bcond_without check
%bcond_with bootstrap
%global debug_package %{nil}
%global module bigquery

%if %{without bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/GoogleCloudPlatform/google-cloud-go
%global goipath         cloud.google.com/go/%{module}
%global forgeurl        https://github.com/GoogleCloudPlatform/google-cloud-go
Version:                1.56.0
%global tag             %{module}/v%{version}
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Google Cloud Client Libraries for Go for module %{module}.}

%global golicenses      LICENSE
%global godocs          CHANGES.md CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        README.md RELEASING.md SECURITY.md testing.md

Name:           %{goname}
Release:        %autorelease
Summary:        Google Cloud Client Libraries for Go for module %{module}

License:        Apache-2.0 AND BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1
find . ! \( -name %{module} -o -name "*.md" -o -name LICENSE -o -name _build \) -maxdepth 1 -exec rm -rf {} \;
mv %{module}/* .

# avoid extra dependencies
rm -rf integration_test.go dataset_integration_test.go routine_integration_test.go params_test.go oc_test.go dataset_test.go storage_bench_test.go storage_integration_test.go table_integration_test.go trace_integration_test.go

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
ln -s /usr/share/gocode/src/cloud.google.com/go/internal _build/src/cloud.google.com/go/
%gocheck
%endif
%endif

%gopkgfiles

%changelog
%autochangelog
