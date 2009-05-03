Summary:	monitrc file for monitoring Quagga routing services
Summary(pl.UTF-8):	Plik monitrc do monitorowania usług routingu Quaggi
Name:		monit-rc-quagga
Version:	1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	quagga-bgpd.monitrc
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	monit
Requires:	monit
Requires:	quagga
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
monitrc file for monitoring Quagga routing services (currently only bgpd).

%description -l pl.UTF-8
Plik monitrc do monitorowania usług routingu Quaggi (obecnie tylko bgpd).

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/monit

install %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/monit

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q monit restart

%postun
%service -q monit restart

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/monit/*.monitrc
