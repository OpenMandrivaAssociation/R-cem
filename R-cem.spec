%global packname  cem
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1.5
Release:          1
Summary:          Coarsened Exact Matching
Group:            Sciences/Mathematics
License:          GPLv2
URL:              http://cran.r-project.org/web/packages/cem/index.html
Source0:          http://cran.r-project.org/src/contrib/cem_1.1.5.tar.gz
BuildRequires:    R-devel R-randomForest R-combinat R-tcltk R-nlme R-lattice
Requires:         R-core R-randomForest R-combinat R-tcltk R-nlme R-lattice
BuildArch:        noarch

%description
Implementation of the Coarsened Exact Matching algorithm

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/makeLelonde.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help