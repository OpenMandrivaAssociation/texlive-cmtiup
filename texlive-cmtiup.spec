%global tl_name cmtiup
%global tl_revision 77050

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Upright punctuation with CM italic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cm/cmtiup
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmtiup.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmtiup.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The cmtiup fonts address a problem with the appearance of punctuation in
italic text in mathematical documents. To achieve this, all punctuation
characters are upright, and kerning between letters and punctuation is
adjusted to allow for the italic correction. The fonts are implemented
as a set of vf files; a package for support in LaTeX2e is provided.

