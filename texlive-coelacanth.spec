%global tl_name coelacanth
%global tl_revision 77682
%global tl_version 0.005

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Coelacanth fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/coelacanth
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/coelacanth.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/coelacanth.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX support for
Coelecanth fonts, designed by Ben Whitmore. Coelacanth is inspired by
the classic Centaur type design of Bruce Rogers, described by some as
the most beautiful typeface ever designed. It aims to be a professional
quality type family for general book typesetting.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from coelacanth:
Map Coelacanth.map
TL_DROPIN_EOF
