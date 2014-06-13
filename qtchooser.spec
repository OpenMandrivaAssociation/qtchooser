Name: qtchooser
Version: 39
Release: 2
Summary: Wrapper used to select between Qt binary versions
Group: System/Libraries
License: GPLv2+
Url: http://www.qt-project.org
Source0: http://macieira.org/qtchooser/%{name}-%{version}-g4717841.tar.xz

%description
The qtchooser package contains a wrapper used to select between
Qt binary versions.

%prep
%setup -q -n %{name}

%build
%make LFLAGS="%{optflags}" CXXFLAGS="%{optflags}"

%install
%make INSTALL_ROOT=%{buildroot} install

mkdir -p %{buildroot}%{_mandir}/man1
install -m644 doc/qtchooser.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}/xdg/qtchooser

%files
%defattr(-,root,root,-)
%{_bindir}/assistant
%{_bindir}/designer
%{_bindir}/lconvert
%{_bindir}/linguist
%{_bindir}/lrelease
%{_bindir}/lupdate
%{_bindir}/moc
%{_bindir}/pixeltool
%{_bindir}/qcollectiongenerator
%{_bindir}/qdbus
%{_bindir}/qdbuscpp2xml
%{_bindir}/qdbusviewer
%{_bindir}/qdbusxml2cpp
%{_bindir}/qdoc
%{_bindir}/qdoc3
%{_bindir}/qglinfo
%{_bindir}/qhelpconverter
%{_bindir}/qhelpgenerator
%{_bindir}/qmake
%{_bindir}/qml
%{_bindir}/qml1plugindump
%{_bindir}/qmlbundle
%{_bindir}/qmlmin
%{_bindir}/qmlplugindump
%{_bindir}/qmlprofiler
%{_bindir}/qmlscene
%{_bindir}/qmltestrunner
%{_bindir}/qmlviewer
%{_bindir}/qtchooser
%{_bindir}/qtconfig
%{_bindir}/rcc
%{_bindir}/uic
%{_bindir}/uic3
%{_bindir}/xmlpatterns
%{_bindir}/xmlpatternsvalidator
%{_sysconfdir}/xdg/qtchooser
%{_mandir}/man1/qtchooser.1*
