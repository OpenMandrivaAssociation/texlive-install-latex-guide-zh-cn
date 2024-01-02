Name:		texlive-install-latex-guide-zh-cn
Version:	69264
Release:	1
Summary:	A short introduction to LaTeX installation written in Chinese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/install-latex-guide-zh-cn
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/install-latex-guide-zh-cn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/install-latex-guide-zh-cn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package will introduce the operations related to
installing TeX Live (introducing MacTeX in macOS), upgrading
macro packages, and compiling simple documents on Windows 10,
Ubuntu 20.04, and macOS systems, and mainly introducing command
line operations.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/install-latex-guide-zh-cn

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
