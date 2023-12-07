# Generated by go2rpm 1.10.0
%bcond_without check
%bcond_without bootstrap
%global debug_package %{nil}

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/google/go-genproto
%global goipath         google.golang.org/genproto
%global forgeurl        https://github.com/google/go-genproto
%global commit          d783a09b4405a1cd1cf45a3ca26e53c9854f603f

%gometa -L

%global common_description %{expand:
This package contains the generated Go packages for common protocol buffer
types, and the generated gRPC code necessary for interacting with Google's gRPC
APIs.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md README.md\\\
                        RELEASING.md SECURITY.md example docs

Name:           golang-google-genproto-googleapis
Version:        0
Release:        %autorelease -b 100
Summary:        Generated code for Google Cloud client libraries

# Upstream license specification: Apache-2.0
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
%autopatch -p1
rm -rf api/apikeys api/servicecontrol api/servicemanagement api/serviceusage

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
