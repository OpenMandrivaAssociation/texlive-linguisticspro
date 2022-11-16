Name:		texlive-linguisticspro
Version:	64858
Release:	1
Summary:	LinguisticsPro fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/linguisticspro
License:	lppl ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linguisticspro.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linguisticspro.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the LinguisticsPro family of fonts. This family is
derived from the Utopia Nova font family, by Andreas Nolda.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/linguisticspro
%{_texmfdistdir}/fonts/vf/public/linguisticspro
%{_texmfdistdir}/fonts/type1/public/linguisticspro
%{_texmfdistdir}/fonts/tfm/public/linguisticspro
%{_texmfdistdir}/fonts/opentype/public/linguisticspro
%{_texmfdistdir}/fonts/map/dvips/linguisticspro
%{_texmfdistdir}/fonts/enc/dvips/linguisticspro
%doc %{_texmfdistdir}/doc/fonts/linguisticspro

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
