#!/bin/bash
set -e

auxfolder=aux_m



echo Cloning projects...
rm -rf $auxfolder
mkdir $auxfolder
cd $auxfolder
git clone git@github.com:killercd/qmail.git

cd ..



