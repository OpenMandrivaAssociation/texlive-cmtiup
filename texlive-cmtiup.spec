Name:		texlive-cmtiup
Version:	2.1
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
%{_texmfdistdir}/fonts/source/public/cmtiup
%{_texmfdistdir}/fonts/tfm/public/cmtiup
%{_texmfdistdir}/fonts/vf/public/cmtiup
%{_texmfdistdir}/tex/latex/cmtiup
%doc %{_texmfdistdir}/doc/latex/cmtiup

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

