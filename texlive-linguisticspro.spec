%global tl_name linguisticspro
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LinguisticsPro fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/linguisticspro
License:	lppl ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/linguisticspro.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/linguisticspro.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the LinguisticsPro family of fonts. This family is derived from the
Utopia Nova font family, by Andreas Nolda.

