Name:		texlive-cmtiup
Version:	39728
Release:	2
Summary:	Upright punctuation with CM slanted
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cm/cmtiup
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmtiup.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmtiup.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The cmtiup fonts address a problem with the appearance of
punctuation in italic text in mathematical documents. To
achieve this, all punctuation characters are upright, and
kerning between letters and punctuation is adjusted to allow
for the italic correction. The fonts are implemented as a set
of vf files; a package for support in LaTeX 2e is provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/cmtiup
%{_texmfdistdir}/fonts/tfm/public/cmtiup
%{_texmfdistdir}/fonts/vf/public/cmtiup
%{_texmfdistdir}/tex/latex/cmtiup
%doc %{_texmfdistdir}/doc/latex/cmtiup

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
