Name:		nosync
Version:	1.1
Release:	4
Summary:	Preload library for disabling file's content synchronization
License:	ASL 2.0
URL:		http://github.com/kjn/%{name}
Source0:	http://github.com/kjn/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: https://github.com/kjn/nosync/pull/4.patch
BuildRequires:	make

%description
nosync is a small preload library that can be used to disable
synchronization of file's content with storage devices on GNU/Linux.
It works by overriding implementations of certain standard functions
like fsync or open.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build CFLAGS="%{optflags}"

%install
install -d %{buildroot}%{_libdir}/nosync
install -p nosync.so %{buildroot}%{_libdir}/nosync/

%files
%doc AUTHORS README.md
%{!?_licensedir:%global license %%doc}
%license LICENSE NOTICE
%{_libdir}/%{name}
