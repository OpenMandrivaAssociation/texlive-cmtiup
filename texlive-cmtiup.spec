# revision 20512
# category Package
# catalog-ctan /fonts/cm/cmtiup
# catalog-date 2010-11-20 14:00:52 +0100
# catalog-license lppl1.3
# catalog-version 1.3a
Name:		texlive-cmtiup
Version:	1.3a
Release:	2
Summary:	Upright punctuation with CM slanted
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cm/cmtiup
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmtiup.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmtiup.doc.tar.xz
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
%{_texmfdistdir}/fonts/source/public/cmtiup/cmtiup10.mf
%{_texmfdistdir}/fonts/source/public/cmtiup/cmtiup12.mf
%{_texmfdistdir}/fonts/source/public/cmtiup/cmtiup7.mf
%{_texmfdistdir}/fonts/source/public/cmtiup/cmtiup8.mf
%{_texmfdistdir}/fonts/source/public/cmtiup/cmtiup9.mf
%{_texmfdistdir}/fonts/source/public/cmtiup/cmtiupgn.mf
%{_texmfdistdir}/fonts/source/public/cmtiup/cmtiuplg.mf
%{_texmfdistdir}/fonts/source/public/cmtiup/cmtiupp.mf
%{_texmfdistdir}/fonts/tfm/public/cmtiup/cmtiup10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmtiup/cmtiup12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmtiup/cmtiup7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmtiup/cmtiup8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmtiup/cmtiup9.tfm
%{_texmfdistdir}/fonts/vf/public/cmtiup/cmtiup10.vf
%{_texmfdistdir}/fonts/vf/public/cmtiup/cmtiup12.vf
%{_texmfdistdir}/fonts/vf/public/cmtiup/cmtiup7.vf
%{_texmfdistdir}/fonts/vf/public/cmtiup/cmtiup8.vf
%{_texmfdistdir}/fonts/vf/public/cmtiup/cmtiup9.vf
%{_texmfdistdir}/tex/latex/cmtiup/cmtiup.sty
%doc %{_texmfdistdir}/doc/latex/cmtiup/README
%doc %{_texmfdistdir}/doc/latex/cmtiup/cmtiup.dtx
%doc %{_texmfdistdir}/doc/latex/cmtiup/cmtiup.ins
%doc %{_texmfdistdir}/doc/latex/cmtiup/cmtiup.pdf
%doc %{_texmfdistdir}/doc/latex/cmtiup/testfont.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3a-2
+ Revision: 750329
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3a-1
+ Revision: 718087
- texlive-cmtiup
- texlive-cmtiup
- texlive-cmtiup
- texlive-cmtiup
- texlive-cmtiup

