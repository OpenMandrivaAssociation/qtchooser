Name:		qtchooser
Version:	66
Release:	2
Summary:	Wrapper used to select between Qt binary versions
Group:		System/Libraries
License:	GPLv2+
Url:		http://www.qt-project.org
Source0:	http://download.qt.io/official_releases/qtchooser/qtchooser-%{version}.tar.xz
Patch0:		qtchooser-66-fix-default.patch

%description
The qtchooser package contains a wrapper used to select between
Qt binary versions.

%prep
%autosetup -p1

%build
%make LFLAGS="%{optflags}" CXXFLAGS="%{optflags}"

%install
%make INSTALL_ROOT=%{buildroot} install

mkdir -p %{buildroot}%{_mandir}/man1
install -m644 doc/qtchooser.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}/xdg/qtchooser

# Get rid of all the qtchooser symlinks, we already
# have symlinks to the "real" tools
cd %{buildroot}%{_bindir}
for i in *; do
	[ "$i" != "qtchooser" ] && rm -f $i
done

%files
%{_bindir}/qtchooser
%{_sysconfdir}/xdg/qtchooser
%{_mandir}/man1/qtchooser.1*
