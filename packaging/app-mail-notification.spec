
Name: app-mail-notification
Epoch: 1
Version: 1.1.2
Release: 1%{dist}
Summary: Mail Notification
License: GPLv3
Group: ClearOS/Apps
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
Requires: %{name}-core = 1:%{version}-%{release}
Requires: app-base

%description
Many apps and services use e-mail to notify administrators of events that may require their attention.  The Mail Notification app ensures that mail can be delivered from your system.

%package core
Summary: Mail Notification - Core
License: LGPLv3
Group: ClearOS/Libraries
Requires: app-base-core
Requires: app-network-core >= 1:1.2.10
Requires: postfix
Requires: Swift

%description core
Many apps and services use e-mail to notify administrators of events that may require their attention.  The Mail Notification app ensures that mail can be delivered from your system.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/mail_notification
cp -r * %{buildroot}/usr/clearos/apps/mail_notification/

install -D -m 0600 packaging/mail_notification.conf %{buildroot}/etc/clearos/mail_notification.conf

%post
logger -p local6.notice -t installer 'app-mail-notification - installing'

%post core
logger -p local6.notice -t installer 'app-mail-notification-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/mail_notification/deploy/install ] && /usr/clearos/apps/mail_notification/deploy/install
fi

[ -x /usr/clearos/apps/mail_notification/deploy/upgrade ] && /usr/clearos/apps/mail_notification/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-mail-notification - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-mail-notification-core - uninstalling'
    [ -x /usr/clearos/apps/mail_notification/deploy/uninstall ] && /usr/clearos/apps/mail_notification/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/mail_notification/controllers
/usr/clearos/apps/mail_notification/htdocs
/usr/clearos/apps/mail_notification/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/mail_notification/packaging
%dir /usr/clearos/apps/mail_notification
/usr/clearos/apps/mail_notification/deploy
/usr/clearos/apps/mail_notification/language
/usr/clearos/apps/mail_notification/libraries
%config(noreplace) /etc/clearos/mail_notification.conf
