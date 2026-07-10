%global tl_name coelacanth
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.005
Release:	%{tl_revision}.1
Summary:	Coelacanth fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/coelacanth
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/coelacanth.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/coelacanth.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX support for
Coelecanth fonts, designed by Ben Whitmore. Coelacanth is inspired by
the classic Centaur type design of Bruce Rogers, described by some as
the most beautiful typeface ever designed. It aims to be a professional
quality type family for general book typesetting.

