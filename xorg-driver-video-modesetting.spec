Summary:	X.org generic video modesetting driver
Name:		xorg-driver-video-modesetting
Version:	0.6.0
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-modesetting-%{version}.tar.bz2
# Source0-md5:	d8a771d5d2d75ea9d234c6928153c08b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	udev-devel
BuildRequires:	xorg-xserver-server-devel
Requires:	xorg-xserver-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an X.org video driver for KMS devices. This is a
non-accelerated driver, the following framebuffer depths are
supported: 8, 15, 16, 24. All visual types are supported for depth 8,
and TrueColor visual is supported for the other depths.  RandR 1.2 is
supported.

%prep
%setup -qn xf86-video-modesetting-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/modesetting_drv.so
%{_mandir}/man4/modesetting.4*

