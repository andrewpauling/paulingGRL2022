#!/bin/bash

if [ ! -f processed.zip ]; then
    echo "Getting CMIP6 data from Zenodo"
    wget https://zenodo.org/record/7553001/files/processed.zip
else
    echo "Already downloaded processed CMIP6 data from Zenodo"
fi

if [ ! -d processed ]; then
    echo "Unzipping CMIP6 data"
    unzip processed.zip
else
    echo "Processed CMIP6 data already unzipped"
fi

if [ ! -d ecsdata ]; then
    echo "Getting ECS data from Mark Zelinka GitHub repo"
    wget https://zenodo.org/record/5206851/files/mzelinka/cmip56_forcing_feedback_ecs-v2.0.zip
    unzip cmip56_forcing_feedback_ecs-v2.0.zip
    mv mzelinka-cmip56_forcing_feedback_ecs-2fc752f ecsdata
else
    echo "Already downloaded ECS data from Mark Zelinka GitHub repo"
fi

if [ ! -d forcingdata ]; then
    echo "Getting Schmidt et al. forcing data"
    mkdir forcingdata
    cd forcingdata
    wget https://gdex.ucar.edu/dataset/2018_Schmidt_JGR_Volcanic_RF/file.zip
    unzip file.zip
    cd ../
else
    echo "Already downloaded Schmidt et al. forcing data"
fi

echo "All data downloaded"
    
