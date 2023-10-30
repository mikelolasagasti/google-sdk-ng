# Generated by go2rpm
%bcond_without check
%bcond_without bootstrap

%if %{without bootstrap}
%global debug_package %{nil}
%endif

# https://github.com/grpc/grpc-go
%global goipath         google.golang.org/grpc
%global forgeurl        https://github.com/grpc/grpc-go
Version:                1.48.0

%gometa

%global common_description %{expand:
The Go language implementation of GRPC, http/2 based rpc.}

# This should be removed in Fedora 39
%global godevelheader0  %{expand:
# This package used to be split up to solve a bootstrapping issue.
# golang-google-grpc-status-devel has since been merged with
# the main -devel package, so we need this to ensure a smooth update path.
# See https://bugzilla.redhat.com/2109630
Provides: golang-google-grpc-status-devel = %{?epoch:epoch:}%{version}-%{release}
Obsoletes: golang-google-grpc-status-devel < 1.48.0-2
}

%global golicenses      LICENSE NOTICE.txt
%global godocs          examples AUTHORS CODE-OF-CONDUCT.md CONTRIBUTING.md\\\
                        GOVERNANCE.md MAINTAINERS.md README.md SECURITY.md\\\
                        Documentation

Name:           %{goname}
Release:        %autorelease -b 43
Summary:        Go language implementation of GRPC

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%if %{without bootstrap}
%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%endif

%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%endif

%if %{without bootstrap}
%if %{with check}
%check
for test in "InvalidMetadata" \
            "SvrWriteStatusEarlyWrite" \
            "AuthorizationEngineEvaluate" \
            "HealthWatchServiceStatusSetBeforeStartingServer" \
            "PolicyEngineEvaluate" \
            "IdentityEncoding" \
            "Fallback" \
            "HealthCheckOff" \
            "ControlChannelCredsFailure" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%endif

%if %{without bootstrap}
%files
%license LICENSE NOTICE.txt
%doc examples AUTHORS CODE-OF-CONDUCT.md CONTRIBUTING.md GOVERNANCE.md
%doc MAINTAINERS.md README.md SECURITY.md Documentation
%{_bindir}/protoc-gen-go-grpc
%endif

%gopkgfiles

%changelog
%autochangelog
