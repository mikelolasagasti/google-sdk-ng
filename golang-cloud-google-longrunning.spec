# Generated by go2rpm 1.9.0
%bcond_with check
%bcond_without bootstrap
%global debug_package %{nil}
%global module longrunning

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/GoogleCloudPlatform/google-cloud-go
%global goipath         cloud.google.com/go/%{module}
%global forgeurl        https://github.com/GoogleCloudPlatform/google-cloud-go
Version:                0.5.3
%global tag             %{module}/v%{version}
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Go packages for Google Cloud Platform services.}


%global golicenses      LICENSE
%global godocs          CHANGES.md CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        README.md RELEASING.md SECURITY.md testing.md\\\

Name:           %{goname}
Release:        %autorelease
Summary:        Google Cloud Client Libraries for Go for module %{module}

License:        BSD-3-Clause AND Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

# remove doc.go from root path to avoid module clash
rm doc.go
# remove all modules but %{module}
find %{_builddir}/google-cloud-go-%{module}-v%{version}/* -depth -type d -not -path '*/%{module}*' -not -path '*/_build*' -exec rm -rf {} \;
# move module to root path to match goipath
mv %{module}/* .

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
