#
# spec file for package python-payload_dumper
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-payload_dumper
Version:        0.2.1
Release:        0
Summary:        File transport adapter for Requests
License:        Apache-2.0
URL:            https://github.com/huakim/payload-dumper
Source:         payload_dumper-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module bsdiff4 >= 1.2.1}
BuildRequires:  %{python_module protobuf >= 3.19.1}
BuildRequires:  %{python_module requests >= 1.0.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-bsdiff4 >= 1.2.1
Requires:       python-enlighten >= 1.10.2
Requires:       python-protobuf >= 3.19.1
Requires:       python-requests >= 1.0.0
BuildArch:      noarch
%python_subpackages

%description
# payload dumper

Dumps the `payload.bin` image found in Android update images. Has significant performance gains over other tools due to using multiprocessing.

## Installation

### Requirements

- Python3
- pip

### Install using pip

```sh
pip install --user payload_dumper
```

## Example ASCIIcast

[![asciicast](https://asciinema.org/a/UbDZGZwCXux50sSzy1fc1bhaO.svg)](https://asciinema.org/a/UbDZGZwCXux50sSzy1fc1bhaO)

## Usage

### Dumping the entirety of `payload.bin`

```
payload_dumper payload.bin
```

### Dumping specific partitions

Use a comma-separated list of partitions to dump:
```
payload_dumper --partitions boot,dtbo,vendor payload.bin
```

### Patching older image with OTA

Assuming the old partitions are in a directory named `old/`:
```
payload_dumper --diff payload.bin
```


%prep
%autosetup -p1 -n payload_dumper-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/executive
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative executive

%postun
%python_uninstall_alternative executive

%files %{python_files}
%doc README.md
%python_alternative %{_bindir}/executive
%{python_sitelib}/payload_dumper
%{python_sitelib}/payload_dumper-%{version}.dist-info

%changelog
