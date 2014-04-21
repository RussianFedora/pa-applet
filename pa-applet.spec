%global commit  33b413b83234d457b9512219cf4c1020eb99a3de
Name:           pa-applet
Version:        0
Release:        1%{?dist}
Summary:        Applet to control PulseAudio volume level and default sink

License:        BSD
URL:            https://github.com/fernandotcl/pa-applet
Source0:        https://github.com/fernandotcl/pa-applet/archive/%{commit}/pa-applet-%{commit}.tar.gz

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(x11)

%description
pa-applet is a systray-applet that allows you to control some of
PulseAudio's features. More specifically, pa-applet allows you to control
the volume level of the default sink and mute or unmute it. It also allows you
to change the active profile of the default sink, which can be useful to tell
PulseAudio to redirect audio to the HDMI output instead of outputting to the
built-in speakers in a computer connected to an HDMI device.

%prep
%setup -qn %{name}-%{commit}

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc README LICENSE ChangeLog
%{_bindir}/pa-applet
%{_mandir}/man1/pa-applet.1.*

%changelog
* Sun Apr 20 2014 Dmitry Melnichenko
- Initial import based on commit 33b413b83234d457b9512219cf4c1020eb99a3de 
