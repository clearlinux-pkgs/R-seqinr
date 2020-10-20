#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-seqinr
Version  : 4.2.4
Release  : 21
URL      : https://cran.r-project.org/src/contrib/seqinr_4.2-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/seqinr_4.2-4.tar.gz
Summary  : Biological Sequences Retrieval and Analysis
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-seqinr-lib = %{version}-%{release}
Requires: R-ade4
Requires: R-segmented
BuildRequires : R-ade4
BuildRequires : R-segmented
BuildRequires : buildreq-R
BuildRequires : pkgconfig(zlib)

%description
for biological sequence (DNA and protein) data. Seqinr includes 
  utilities for sequence data management under the ACNUC system
  described in Gouy, M. et al. (1984) Nucleic Acids Res.

%package lib
Summary: lib components for the R-seqinr package.
Group: Libraries

%description lib
lib components for the R-seqinr package.


%prep
%setup -q -c -n seqinr
cd %{_builddir}/seqinr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602524520

%install
export SOURCE_DATE_EPOCH=1602524520
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library seqinr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library seqinr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library seqinr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc seqinr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/seqinr/CITATION
/usr/lib64/R/library/seqinr/DESCRIPTION
/usr/lib64/R/library/seqinr/INDEX
/usr/lib64/R/library/seqinr/Meta/Rd.rds
/usr/lib64/R/library/seqinr/Meta/data.rds
/usr/lib64/R/library/seqinr/Meta/features.rds
/usr/lib64/R/library/seqinr/Meta/hsearch.rds
/usr/lib64/R/library/seqinr/Meta/links.rds
/usr/lib64/R/library/seqinr/Meta/nsInfo.rds
/usr/lib64/R/library/seqinr/Meta/package.rds
/usr/lib64/R/library/seqinr/NAMESPACE
/usr/lib64/R/library/seqinr/NEWS
/usr/lib64/R/library/seqinr/R/seqinr
/usr/lib64/R/library/seqinr/R/seqinr.rdb
/usr/lib64/R/library/seqinr/R/seqinr.rdx
/usr/lib64/R/library/seqinr/abif/1_0000206138_C01_005.fsa
/usr/lib64/R/library/seqinr/abif/1_FAC321_0000205983_B02_004.fsa
/usr/lib64/R/library/seqinr/abif/2_0000206138_C01_005.fsa
/usr/lib64/R/library/seqinr/abif/2_FAC321_0000205983_B02_004.fsa
/usr/lib64/R/library/seqinr/abif/AmpFLSTR_Bins_v1.txt
/usr/lib64/R/library/seqinr/abif/AmpFLSTR_Panels_v1.txt
/usr/lib64/R/library/seqinr/abif/NGM_Bins.txt
/usr/lib64/R/library/seqinr/abif/NGM_Pa.txt
/usr/lib64/R/library/seqinr/abif/Promega_Bins_v1.txt
/usr/lib64/R/library/seqinr/abif/Promega_Panels_v1.txt
/usr/lib64/R/library/seqinr/abif/Prototype_PowerPlex_EP01_Bins.txt
/usr/lib64/R/library/seqinr/abif/Prototype_PowerPlex_EP01_Pa.txt
/usr/lib64/R/library/seqinr/abif/samplefsa2ps.fsa
/usr/lib64/R/library/seqinr/data/AnoukResult.RData
/usr/lib64/R/library/seqinr/data/ECH.RData
/usr/lib64/R/library/seqinr/data/EXP.RData
/usr/lib64/R/library/seqinr/data/JLO.RData
/usr/lib64/R/library/seqinr/data/SEQINR.UTIL.RData
/usr/lib64/R/library/seqinr/data/aacost.RData
/usr/lib64/R/library/seqinr/data/aaindex.RData
/usr/lib64/R/library/seqinr/data/caitab.RData
/usr/lib64/R/library/seqinr/data/chargaff.RData
/usr/lib64/R/library/seqinr/data/clustal.RData
/usr/lib64/R/library/seqinr/data/datalist
/usr/lib64/R/library/seqinr/data/dinucl.RData
/usr/lib64/R/library/seqinr/data/ec999.RData
/usr/lib64/R/library/seqinr/data/fasta.RData
/usr/lib64/R/library/seqinr/data/gcO2.rda
/usr/lib64/R/library/seqinr/data/gcT.rda
/usr/lib64/R/library/seqinr/data/gs500liz.RData
/usr/lib64/R/library/seqinr/data/identifiler.RData
/usr/lib64/R/library/seqinr/data/kaksTorture.RData
/usr/lib64/R/library/seqinr/data/m16j.RData
/usr/lib64/R/library/seqinr/data/mase.RData
/usr/lib64/R/library/seqinr/data/msf.RData
/usr/lib64/R/library/seqinr/data/pK.RData
/usr/lib64/R/library/seqinr/data/phylip.RData
/usr/lib64/R/library/seqinr/data/prochlo.RData
/usr/lib64/R/library/seqinr/data/revaligntest.RData
/usr/lib64/R/library/seqinr/data/sysdata.rda
/usr/lib64/R/library/seqinr/data/toyaa.RData
/usr/lib64/R/library/seqinr/data/toycodon.RData
/usr/lib64/R/library/seqinr/data/waterabs.RData
/usr/lib64/R/library/seqinr/help/AnIndex
/usr/lib64/R/library/seqinr/help/aliases.rds
/usr/lib64/R/library/seqinr/help/figures/aka.pdf
/usr/lib64/R/library/seqinr/help/figures/chargaff.png
/usr/lib64/R/library/seqinr/help/figures/gcskewmbe96.pdf
/usr/lib64/R/library/seqinr/help/figures/introduction-dbg.pdf
/usr/lib64/R/library/seqinr/help/figures/lncs2004.pdf
/usr/lib64/R/library/seqinr/help/figures/waterabs.jpg
/usr/lib64/R/library/seqinr/help/paths.rds
/usr/lib64/R/library/seqinr/help/seqinr.rdb
/usr/lib64/R/library/seqinr/help/seqinr.rdx
/usr/lib64/R/library/seqinr/html/00Index.html
/usr/lib64/R/library/seqinr/html/R.css
/usr/lib64/R/library/seqinr/sequences/Anouk.fasta
/usr/lib64/R/library/seqinr/sequences/DarrenObbard.fasta
/usr/lib64/R/library/seqinr/sequences/ECOUNC.fsa
/usr/lib64/R/library/seqinr/sequences/LTPs128_SSU_aligned_First_Two.fasta
/usr/lib64/R/library/seqinr/sequences/UBIQUITIN.mase
/usr/lib64/R/library/seqinr/sequences/ame1.gbk
/usr/lib64/R/library/seqinr/sequences/bb.acc
/usr/lib64/R/library/seqinr/sequences/bb.kwd
/usr/lib64/R/library/seqinr/sequences/bb.mne
/usr/lib64/R/library/seqinr/sequences/bb.sp
/usr/lib64/R/library/seqinr/sequences/bordetella.fasta
/usr/lib64/R/library/seqinr/sequences/bordetella.pep.aln
/usr/lib64/R/library/seqinr/sequences/ct.bfa
/usr/lib64/R/library/seqinr/sequences/ct.fasta.gz
/usr/lib64/R/library/seqinr/sequences/ct.gbk.gz
/usr/lib64/R/library/seqinr/sequences/ct.predict
/usr/lib64/R/library/seqinr/sequences/ecolicgpe5.fasta
/usr/lib64/R/library/seqinr/sequences/gopher.fasta
/usr/lib64/R/library/seqinr/sequences/gopher.names
/usr/lib64/R/library/seqinr/sequences/hannah.txt
/usr/lib64/R/library/seqinr/sequences/humanMito.fasta
/usr/lib64/R/library/seqinr/sequences/input.dat
/usr/lib64/R/library/seqinr/sequences/input.out
/usr/lib64/R/library/seqinr/sequences/kaks-torture.fasta
/usr/lib64/R/library/seqinr/sequences/legacy.fasta
/usr/lib64/R/library/seqinr/sequences/louse.fasta
/usr/lib64/R/library/seqinr/sequences/louse.names
/usr/lib64/R/library/seqinr/sequences/malM.fasta
/usr/lib64/R/library/seqinr/sequences/ortho.fasta
/usr/lib64/R/library/seqinr/sequences/scuco.txt
/usr/lib64/R/library/seqinr/sequences/seqAA.fasta
/usr/lib64/R/library/seqinr/sequences/smallAA.fasta
/usr/lib64/R/library/seqinr/sequences/smallAA.fasta.gz
/usr/lib64/R/library/seqinr/sequences/someORF.fsa
/usr/lib64/R/library/seqinr/sequences/test.aln
/usr/lib64/R/library/seqinr/sequences/test.mase
/usr/lib64/R/library/seqinr/sequences/test.msf
/usr/lib64/R/library/seqinr/sequences/test.phylip

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/seqinr/libs/seqinr.so
/usr/lib64/R/library/seqinr/libs/seqinr.so.avx2
/usr/lib64/R/library/seqinr/libs/seqinr.so.avx512
