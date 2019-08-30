#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-stringtemplate4
Version  : 4.0.4
Release  : 2
URL      : https://github.com/antlr/website-st4/raw/gh-pages/download/ST-4.0.4-src.zip
Source0  : https://github.com/antlr/website-st4/raw/gh-pages/download/ST-4.0.4-src.zip
Source1  : https://repo1.maven.org/maven2/org/antlr/ST4/4.0.4/ST4-4.0.4.jar
Source2  : https://repo1.maven.org/maven2/org/antlr/ST4/4.0.4/ST4-4.0.4.pom
Source3  : https://repo1.maven.org/maven2/org/antlr/ST4/4.0.8/ST4-4.0.8.jar
Source4  : https://repo1.maven.org/maven2/org/antlr/ST4/4.0.8/ST4-4.0.8.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-stringtemplate4-data = %{version}-%{release}

%description
StringTemplate 4.0.3
June 21, 2011
Terence Parr, parrt at cs usfca edu
ANTLR project lead and supreme dictator for life
University of San Francisco

%package data
Summary: data components for the mvn-stringtemplate4 package.
Group: Data

%description data
data components for the mvn-stringtemplate4 package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/ST4/4.0.4
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/antlr/ST4/4.0.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/ST4/4.0.4
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/antlr/ST4/4.0.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/ST4/4.0.8
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/antlr/ST4/4.0.8

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/antlr/ST4/4.0.8
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/antlr/ST4/4.0.8


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/antlr/ST4/4.0.4/ST4-4.0.4.jar
/usr/share/java/.m2/repository/org/antlr/ST4/4.0.4/ST4-4.0.4.pom
/usr/share/java/.m2/repository/org/antlr/ST4/4.0.8/ST4-4.0.8.jar
/usr/share/java/.m2/repository/org/antlr/ST4/4.0.8/ST4-4.0.8.pom
