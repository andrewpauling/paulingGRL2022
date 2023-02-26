from model import Model

models = [
    "ACCESS-ESM1-5",
    "CanESM5",
    "CESM2",
    "CNRM-CM6-1",
    "EC-Earth3",
    "GISS-E2-1-G",
    "GISS-E2-1-H",
    "INM-CM5-0",
    "IPSL-CM6A-LR",
    "MIROC-ES2L",
    "MIROC6",
    "MPI-ESM1-2-HR",
    "MPI-ESM1-2-LR",
    "MRI-ESM2-0",
    "NorCPM1",
    "UKESM1-0-LL"
]

experiments = ["historical", "abrupt-4xCO2"]

variables = ["tas"]

for modelname in models:
    for experiment in experiments:
        for var in variables:
            model = Model(modelname, experiment, var)
            print(model)

            model.process_data()
