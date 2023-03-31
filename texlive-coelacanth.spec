Name:		texlive-coelacanth
Version:	64558
Release:	2
Summary:	Coelacanth fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/coelacanth
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coelacanth.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coelacanth.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX
support for Coelecanth fonts, designed by Ben Whitmore.
Coelacanth is inspired by the classic Centaur type design of
Bruce Rogers, described by some as the most beautiful typeface
ever designed. It aims to be a professional quality type family
for general book typesetting.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/coelacanth
%{_texmfdistdir}/fonts/vf/public/coelacanth
%{_texmfdistdir}/fonts/type1/public/coelacanth
%{_texmfdistdir}/fonts/tfm/public/coelacanth
%{_texmfdistdir}/fonts/opentype/public/coelacanth
%{_texmfdistdir}/fonts/map/dvips/coelacanth
%{_texmfdistdir}/fonts/enc/dvips/coelacanth
%doc %{_texmfdistdir}/doc/fonts/coelacanth

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
