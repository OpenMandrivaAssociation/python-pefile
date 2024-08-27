Name:           python-pefile
Version:        2024.8.26
Release:        1
Summary:        A python module to work with PE (pertable executable) files
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/erocarrera/pefile
Source:         https://files.pythonhosted.org/packages/source/p/pefile/pefile-%{version}.tar.gz
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(future)

Requires:       python3dist(future)

BuildArch:      noarch

%description
Portable Executable reader module.

All the PE file basic structures are available with their default names as
attributes of the instance returned.

Processed elements such as the import table are made available with lowercase
names, to differentiate them from the upper case basic structure names.

pefile has been tested against many edge cases such as corrupted and malformed
PEs as well as malware, which often attempts to abuse the format way beyond its
standard use. To the best of my knowledge most of the abuse is handled
gracefully.

%prep
%autosetup -n pefile-%{version} -p1
sed -i -e '/^#!\//, 1d' pefile.py

%build
%py_build

%install
%py_install

%files
%{python_sitelib}/pefile-%{version}-py*.*.egg-info
%{python_sitelib}/pefile.py
%{python_sitelib}/peutils.py
%{python_sitelib}/ordlookup/
