#!/bin/bash

echo "Start by A_vis";
./runCards_Avis.sh;
echo "Other masses";
./runCards_Amasses.sh;
echo "Other masses, no zero masses";
./runCards_Amasses_noZero.sh;
echo "A constrained with H vis constrained":
./runCards_Aconstrained.sh;
echo "A constrained with H svFit constrained":
./runCards_Aconstrained_svFit.sh;

